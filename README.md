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
- [ ] Python ETL Script Implementation.
- [ ] Automated Progressive Overload Alerts.

