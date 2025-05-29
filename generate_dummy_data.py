import pandas as pd
import random
from datetime import datetime, timedelta

# Generate dummy data
num_rows = 100
data = {
    "timestamp": [datetime.now() - timedelta(minutes=random.randint(0, 1000)) for _ in range(num_rows)],
    "level": [random.choice(["INFO", "WARNING", "ERROR"]) for _ in range(num_rows)],
    "message": [f"Log message {i}" for i in range(num_rows)],
    "is_anomaly": [random.choice([True, False]) for _ in range(num_rows)],
    "message_length": [random.randint(20, 100) for _ in range(num_rows)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("dummy_processed_logs.csv", index=False)
print("Dummy file 'dummy_processed_logs.csv' created successfully!")