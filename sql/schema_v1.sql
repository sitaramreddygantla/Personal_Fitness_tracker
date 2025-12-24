/* PROJECT: Personal Fitness Tracker - Database Schema v1
   AUTHOR: SETHARAMA REDDY GANTLA
   DATE: 2025-12-24
   
   CHANGELOG:
   1. Initial creation of 'workouts' table.
   2. Added 'exercise_name' via ALTER TABLE.
   3. Created 'v_workouts' view to fix column display order.
   4. Refined Primary Key: Migrated from 'workout_id' to a Composite Key 
      (log_date, exercise_name, set_number) for better data integrity.
   5. Created 'nutrition' table for macro tracking.
*/

-- STEP 1: Initial Workouts Table
CREATE TABLE workouts (
    workout_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(50),
    body_part VARCHAR(50),
    set_number INTEGER,
    weight DECIMAL,
    reps SMALLINT
);

-- STEP 2: Adding the missing exercise column
ALTER TABLE workouts ADD COLUMN exercise VARCHAR(50);

-- STEP 3: Creating a View for better column ordering
-- This ensures 'exercise_name' appears in the middle for reporting.
CREATE VIEW v_workouts AS
SELECT workout_id, date, exercise, category, body_part, set_number, weight, reps
FROM workouts;

-- STEP 4: Upgrading to a Composite Primary Key
-- Dropping the auto-generated ID and enforcing uniqueness on Date+Exercise+Set
ALTER TABLE workouts
	DROP CONSTRAINT workouts_pkey,	
	DROP COLUMN workout_id,
	ADD primary key (date, exercise, set_number);

-- STEP 5: Creating the Nutrition Table
CREATE TABLE nutrition (
    date DATE PRIMARY KEY,
    weight DECIMAL(5,2) NOT NULL,
    calories DECIMAL(7,2) NOT NULL,
    protein DECIMAL(5,2) NOT NULL,
    fats DECIMAL(5,2) NOT NULL,
    carbs DECIMAL(5,2) NOT NULL,
    fiber DECIMAL(5,2) NOT NULL
);

-- UPDATE [24-12-2025]: Renamed 'date' to 'log_date' for better SQL compliance.
-- Updating the view to reflect this change
-- Note: OR REPLACE cannot change column names in a view. Recreated view to reflect table column rename (date -> log_date).
-- 1. Remove the old version entirely
DROP VIEW v_workouts;

-- 2. Create the new version with the correct column names
CREATE VIEW v_workouts AS
SELECT 
    log_date,
    category,
    body_part,
    exercise, 
    set_number,
    weight,
    reps
FROM workouts;

-- UPDATE [24-12-2025]: Renamed 'weight' to 'body_weight' in nutrition table to avoid mix-up with weight in workouts table
ALTER TABLE nutrition
RENAME COLUMN weight TO body_weight

-- UPDATE [24-12-2025]: Renamed 'date' to 'log_date' in nutrition table for better SQL compliance. 
ALTER TABLE nutrition
RENAME COLUMN date TO log_date;
