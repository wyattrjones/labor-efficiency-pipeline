import os
import sqlite3
import pandas as pd

DB_PATH = "data/workforce.db"
CSV_PATH = "data/raw_timecard_logs.csv"

def process_and_load_data():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found. Make sure your data is generated first!")
        return

    # 1. Read Raw CSV Data
    print("Loading raw timecard logs...")
    df = pd.read_csv(CSV_PATH)

    # 2. Connect to SQLite Database (creates it if it doesn't exist)
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    
    # 3. Load raw data into SQLite table
    df.to_sql("raw_timecards", conn, if_exists="replace", index=False)
    print("Successfully loaded raw data into SQLite table 'raw_timecards'.")

    # 4. Process & Calculate Labor Efficiency Metrics via SQL
    query = """
    SELECT 
        department,
        COUNT(employee_id) as total_employees,
        SUM(regular_hours) as total_regular_hours,
        SUM(overtime_hours) as total_overtime_hours,
        ROUND(SUM(overtime_hours * hourly_rate * 1.5), 2) as estimated_ot_cost
    FROM raw_timecards
    GROUP BY department
    ORDER BY estimated_ot_cost DESC;
    """
    
    summary_df = pd.read_sql(query, conn)
    
    # Save processed summary table back to database
    summary_df.to_sql("dept_labor_summary", conn, if_exists="replace", index=False)
    
    print("\n--- Department Labor Cost Leakage Summary ---")
    print(summary_df)

    conn.close()
    print(f"\nPipeline execution complete. Database saved to '{DB_PATH}'.")

if __name__ == "__main__":
    process_and_load_data()
