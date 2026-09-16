import os
import random
import pandas as pd

# Set seed for reproducibility
random.seed(42)

# Configuration
NUM_RECORDS = 500
DEPARTMENTS = ["Operations", "Logistics", "Customer Support", "Facilities", "Human Resources"]
PAY_TYPES = ["Hourly", "Salaried"]
SHIFT_TYPES = ["Day", "Night", "Weekend Differential"]

def generate_timecard_data(num_rows):
    data = []
    for i in range(1, num_rows + 1):
        emp_id = f"EMP-{1000 + i}"
        dept = random.choice(DEPARTMENTS)
        pay_type = random.choices(PAY_TYPES, weights=[0.8, 0.2], k=1)[0]
        
        if pay_type == "Hourly":
            hourly_rate = round(random.uniform(18.0, 35.0), 2)
            regular_hours = 40.0
            # Simulate occasional unauthorized or high overtime spikes
            overtime_hours = round(random.choice([0, 0, 2.5, 5.0, 8.5, 12.0]), 1)
        else:
            hourly_rate = round(random.uniform(30.0, 55.0), 2)
            regular_hours = 40.0
            overtime_hours = 0.0 # Exempt employees don't track standard overtime
            
        shift_type = random.choice(SHIFT_TYPES)
        approval_status = "Approved" if overtime_hours < 6.0 else random.choice(["Approved", "Flagged-Manager Review"])
        
        data.append({
            "employee_id": emp_id,
            "department": dept,
            "pay_type": pay_type,
            "regular_hours": regular_hours,
            "overtime_hours": overtime_hours,
            "hourly_rate": hourly_rate,
            "shift_type": shift_type,
            "approval_status": approval_status
        })
        
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Generate dataset
    df = generate_timecard_data(NUM_RECORDS)
    
    # Save to CSV
    output_path = "data/raw_timecard_logs.csv"
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {NUM_RECORDS} mock timecard records at '{output_path}'.")
