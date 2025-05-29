import pandas as pd
from sklearn.ensemble import IsolationForest
import os

# === 1. Read Log File ===
log_file = "system_logs.txt"
if not os.path.exists(log_file):
    raise FileNotFoundError(f"{log_file} not found.")

with open(log_file, "r") as file:
    log_entries = file.readlines()

# === 2. Parse Logs into DataFrame ===
data = []
for log in log_entries:
    parts = log.strip().split(" ", 3)
    if len(parts) < 4:
        continue
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3]
    data.append([timestamp, level, message])

df = pd.DataFrame(data, columns=["timestamp", "level", "message"])
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df.dropna(subset=["timestamp"], inplace=True)

# === 3. Feature Engineering ===
level_mapping = {"INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
df["level_score"] = df["level"].map(level_mapping)
df["message_length"] = df["message"].apply(len)

# === 4. Anomaly Detection using Isolation Forest ===
model = IsolationForest(contamination=0.1, random_state=42)
df["anomaly_score"] = model.fit_predict(df[["level_score", "message_length"]])
df["is_anomaly"] = df["anomaly_score"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

# === 5. Save Processed Data for Streamlit Dashboard ===
output_csv = "processed_logs.csv"
df.to_csv(output_csv, index=False)
print(f"✅ Processed log data saved to {output_csv}")
print(f"🚨 {df['is_anomaly'].value_counts().get('Anomaly', 0)} anomalies detected.")
