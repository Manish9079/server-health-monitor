🖥️ Server Health Monitoring System
🚀 Overview

This project is a simple DevOps-based System Health Monitoring Tool built using Python.
It continuously monitors system performance like CPU, RAM, and Disk usage and logs the data for analysis.

🎯 Features
🟢 Real-time CPU usage monitoring
🟢 RAM usage tracking
🟢 Disk space monitoring
🟢 Health status (Healthy / Warning / Critical)
📝 Automatic logging system
⏱️ Runs continuously or via cron job
🧰 Tech Stack
Python 🐍
psutil library
Linux (Kali/Ubuntu)
Cron Jobs (Automation)
📁 Project Structure
server-health-monitor/
│
├── health_monitor.py        # Main monitoring script
├── health_dashboard.html    # Simple dashboard UI
├── server_health.log       # Logs file
└── README.md               # Documentation
▶️ How to Run
1. Install dependencies
pip install psutil
2. Run monitoring script
python3 health_monitor.py
3. Open dashboard
xdg-open health_dashboard.html
⏱️ Automation (Cron Job)

Run every 10 minutes:

crontab -e

Add this line:

*/10 * * * * python3 /path/to/health_monitor.py >> /path/to/server_health.log 2>&1
📊 Output Example
CPU Usage: 3.6% 🟢 HEALTHY
RAM Usage: 38.3% 🟢 HEALTHY
Disk Usage: 9.7% 🟢 HEALTHY
💡 Learning Outcomes
Understanding system monitoring in DevOps
Basics of automation using cron jobs
Working with Python system libraries
Logging and real-time data tracking
📸 Screenshot

(Add your terminal/dashboard screenshot here)

🔥 Future Improvements
📊 Grafana dashboard integration
📩 Email alerts for high CPU/RAM
☁️ AWS cloud deployment
🐳 Docker containerization
👨‍💻 Author

Manish Kumawat
BCA Student | Aspiring DevOps Engineer
