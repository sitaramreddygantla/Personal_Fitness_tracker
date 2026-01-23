import psycopg2 as pg2
from psycopg2 import extras
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

#1. Database connection configuration
DB_CONFIG = {
            "host":"localhost",
            "database":"Fitness Tracker",
            "user":os.getenv("DB_USER"),
            "password":os.getenv("DB_PASSWORD"),
            "port":'5432'
            }

#2. 'Level Up' logic
def get_performance_alerts():
    query = """
               WITH weekly_vol AS (
                SELECT exercise, DATE_TRUNC('week', log_date) AS week_st,  
                SUM(weight*reps) AS volume_cur
                FROM workouts
                GROUP BY week_st, exercise
                ORDER BY week_st, exercise
                ),

                monthly_vol AS (
                SELECT exercise, week_st,
                DATE_TRUNC('month', week_st) AS month_st, volume_cur,
                LAG (volume_cur,1,0) OVER(PARTITION BY exercise ORDER BY week_st) AS vol_1prev_week,
                LAG (volume_cur,2,0) OVER(PARTITION BY exercise ORDER BY week_st) AS vol_2prev_week,
                ROUND(AVG(volume_cur) OVER(PARTITION BY DATE_TRUNC('month', week_st)),2) AS month_vol
                FROM weekly_vol
                ORDER BY exercise
                ),

                final_advice AS (
                SELECT exercise, week_st,
                CASE 
                        WHEN ((month_vol < volume_cur) AND (month_vol < vol_1prev_week) AND (month_vol < vol_2prev_week)) THEN 'increase'
                        ELSE 'continue'
                        END AS advise
                FROM monthly_vol
                ORDER BY exercise
                )

                SELECT exercise FROM final_advice 
                        WHERE advise = 'increase' 
                        AND week_st = DATE_TRUNC('week',CURRENT_DATE);
            """
    try:
        conn = pg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory = extras.DictCursor)
        cur.execute(query)
        results = cur.fetchall()

        if results:
            print("🚀 PROGRESSIVE OVERLOAD ALERTS:")
            for row in results:
                print(f"Time to increase weight on: {row['exercise']}")
        else:
            print("No increases triggered. Keep grinding!")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    get_performance_alerts()
