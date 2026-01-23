# Personal_Fitness_tracker
An end-to-end data pipeline that synchronizes fitness and nutrition data from Google Sheets to a PostgreSQL database using Python, featuring automated progressive overload logic and data integrity constraints.

## 🏗 Project Architecture
1. Source: Manual logging in Google Sheets (Mobile-friendly for the gym).
2. Orchestration: Python scripts using `gspread` (Extract) and `psycopg2` (Load).
3. Storage: PostgreSQL database with a normalized schema and composite keys.
4. Analysis: SQL queries to monitor volume, PRs, and progressive overload cycles.

## 🛠 Tech Stack
- Database: PostgreSQL
- Language: Python 3.13
- APIs: Google Sheets API & Google Drive API
- Version Control: Git & GitHub

## 📂 Local Environment Setup
The project is structured locally on macOS to maintain security and organization:
- `sql/`: Contains all DDL (Data Definition Language) files and schema versions.
- `scripts/`: Python ETL scripts for data synchronization.
- `credentials/`: Secure storage for API keys (ignored by Git for security).

## 📈 Project Status: Phase 1 (Database & Infrastructure)
- [x] Database Schema Design (Workouts & Nutrition tables).
- [x] Local Environment Configuration (Folder architecture & Git cloning).
- [x] Version Control Setup (Handling hidden `.git` and `.gitignore` files).
- [x] Google Cloud API Authentication.
- [x] Python ETL Script Implementation.

## 📈 Project Status: Phase 2 (Analytical Logic & Insights)
- [x] Advanced SQL Analytical Engine
   -> Developed a 15-question challenge framework to stress-test workout data.
   -> Implemented Window Functions for performance benchmarking (e.g., comparing weekly volume vs. monthly averages).
   -> Integrated Statistical Measures ($STDDEV$, Median, Mode) to track accessory exercise consistency.
- [x] Complex Pattern Recognition
   -> Solved the "Gaps and Islands" problem to identify consecutive progressive overload streaks.
   -> Automated "Spike Detection" logic to flag high-intensity overreach weeks (1.2x volume threshold).

## 📈 Project Status: Phase 3 (Automation & UX)
- [x] Scripts for Automated Progressive Overload Alerts.
- [ ] Slack/Email integration for weekly progress summaries.
- [ ] Logic for "Deload Week" suggestions if volume drops by >30%.

