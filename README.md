# Labor Efficiency & Cost Leakage Pipeline

## 📊 Executive Power BI Dashboard

![Labor Efficiency Dashboard](docs/dashboard_preview.png)

An automated HRIS and People Analytics pipeline built to ingest raw timecard logs, load them into a relational database, and transform the data to identify labor cost leakage (specifically excessive overtime and operational inefficiencies) by department.

## Project Overview
In human resources and workforce management, uncontrolled overtime and scheduling inefficiencies are major drivers of budget leakage. This project simulates an enterprise timecard tracking system to demonstrate end-to-end data engineering capabilities:
* **Data Generation:** Programmatically builds realistic, messy raw timecard logs with varying shift durations, breaks, and department structures.
* **ETL & Storage:** Cleans and loads the raw logs into a localized SQLite database (`workforce.db`) using Python and Pandas.
* **SQL Transformation:** Executes analytical queries to aggregate metrics, calculate overtime costs, and flag cost-leakage hotspots.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, SQLite3
* **Database:** SQLite
* **Version Control:** Git & GitHub


