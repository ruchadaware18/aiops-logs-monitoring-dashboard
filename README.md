# 🔍 AIOps Log Monitoring & Anomaly Detection Dashboard

An interactive **Streamlit-based dashboard** for analyzing and detecting anomalies in system logs using machine learning (Isolation Forest). This project demonstrates AIOps capabilities with log parsing, anomaly detection, and rich visualizations for IT operations and infrastructure monitoring.

---

## 🚀 Features

- ✅ **User-uploaded log ingestion** (`.csv`)
- 🧠 **Anomaly detection** using Isolation Forest
- 📈 **Time series plot** of log volume
- 🌡️ **Anomaly heatmap** (hour vs day)
- 📊 **Log level bar chart**
- 🔎 **Filterable log table** with anomaly tags
- 📥 Export filtered logs as `.csv`
- 📁 Fallback to default logs if none uploaded

---

## 🧰 Tech Stack

| Tool/Library     | Purpose                                  |
|------------------|-------------------------------------------|
| Python           | Core scripting and data processing        |
| Pandas           | DataFrame operations and preprocessing    |
| Scikit-learn     | Isolation Forest for anomaly detection    |
| Streamlit        | Frontend dashboard (interactive UI)       |
| Altair           | Time series & heatmap visualizations      |
| Matplotlib/Seaborn| Optional charting (if extended)          |

---


---

## 🔧 How It Works

1. **Upload a Log File (`.csv`)**
   - Must include `timestamp`, `level`, and `message` columns
   - Auto-parsed and converted to structured DataFrame

2. **Anomaly Detection**
   - Log levels are converted to scores
   - Message lengths are calculated
   - Isolation Forest flags unusual patterns

3. **Visual Analysis**
   - 📈 Time series: Log volume trends
   - 🌡️ Heatmap: Anomalies by hour/day
   - 📋 Table: All logs with anomaly classification

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aiops-log-dashboard.git
cd aiops-log-dashboard
```

### 2. Install Dependencies
Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # or .\venv\Scripts\activate on Windows
```

Install packages:
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

### 4. Upload Your Log File
- Format: .csv
- Required columns: timestamp, level, message


📈 Future Enhancements
- Real-time log ingestion (Kafka/S3)
- NLP-based log message clustering
- Email/Slack alerts on anomaly spikes
- User authentication & role-based access
- Dockerized deployment


## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change or improve.


Built with ❤️ by Rucha Daware





