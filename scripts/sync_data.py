import gspread
import psycopg2 as pg2
#For hiding my user and password data
import os
from dotenv import load_dotenv
# To look for .env file in the same folder as sync_data.py
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)


def sync():
    try:
        # 1. Tell Python where your key is
        gc = gspread.service_account(filename='credentials/service_account.json')
        print("✅ Step 1: Authentication Successful!")

        # 2. Try to open your specific Google Sheet
        sh = gc.open('My Fitness Tracker') 
        worksheet = sh.sheet1
        
        # 3. Grab the rows from My fitness tracker worksheet
        data = worksheet.get_all_records() #Turns the sheet into a list of dictionaries.

        # 4. Connection (Postgres) and emptying the table of earlier logs.
        # TRUNCATE TABLE is quicker than DELETE and resets the serial key too
        conn = pg2.connect(database = 'Fitness Tracker', host = 'localhost', user = os.getenv("DB_USER"), password = os.getenv("DB_PASSWORD"), port = '5432')
        cur = conn.cursor()

        #Setting the datetime style to DD-MM-YYYY against the universal default YYYY-MM-DD
        cur.execute("SET Datestyle TO 'DMY';")
        cur.execute('TRUNCATE TABLE workouts RESTART IDENTITY;')

        # 5. Populating the workouts table in database
        for row in data:
            cur.execute("""INSERT INTO workouts (log_date, category, body_part, exercise, set_number, weight, reps)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)""", (row['log_date'], row['category'], row['body_part'],row['exercise'],row['set_number'],row['weight'],row['reps']))

        conn.commit()
        print(f"✅ Success! {len(data)} rows synced to the 'workouts' table.")

    except Exception as e:
        print(f"❌ sync failed: {e}")

    finally:
        #6. Closing the cursor and connection by checking the locals() dictionary.
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    sync()
