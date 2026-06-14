#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   AUTO SERVER HEALTH MONITOR v1.0        ║
║   CPU | RAM | DISK — Log + Status        ║
╚══════════════════════════════════════════╝
"""

import psutil
import time
import datetime
import os
import sys

# ─── CONFIG ───────────────────────────────
LOG_FILE      = "server_health.log"
CHECK_INTERVAL = 10          # seconds
CPU_WARN      = 60           # %
CPU_CRIT      = 85
RAM_WARN      = 70
RAM_CRIT      = 90
DISK_WARN     = 75
DISK_CRIT     = 90
# ──────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
DIM    = "\033[2m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def bar(val, warn, crit, width=20):
    filled = int(val / 100 * width)
    if val >= crit:
        color = RED
    elif val >= warn:
        color = YELLOW
    else:
        color = GREEN
    return f"{color}{'█' * filled}{'░' * (width - filled)}{RESET}"

def status_label(val, warn, crit):
    if val >= crit:
        return f"{RED}🔴 CRITICAL{RESET}"
    elif val >= warn:
        return f"{YELLOW}🟡 WARNING {RESET}"
    else:
        return f"{GREEN}🟢 HEALTHY {RESET}"

def get_metrics():
    cpu  = psutil.cpu_percent(interval=1)
    ram  = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return {
        "cpu_pct" : cpu,
        "ram_pct" : ram.percent,
        "ram_used": ram.used  // (1024**2),
        "ram_total": ram.total // (1024**2),
        "disk_pct": disk.percent,
        "disk_used": disk.used  // (1024**3),
        "disk_total": disk.total // (1024**3),
    }

def write_log(ts, m):
    line = (f"[{ts}] "
            f"CPU={m['cpu_pct']}% "
            f"RAM={m['ram_pct']}%({m['ram_used']}MB/{m['ram_total']}MB) "
            f"DISK={m['disk_pct']}%({m['disk_used']}GB/{m['disk_total']}GB)\n")
    with open(LOG_FILE, "a") as f:
        f.write(line)

def display(m, ts, run):
    clear()
    print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║   🖥️  AUTO SERVER HEALTH MONITOR  v1.0       ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════╝{RESET}")
    print(f"{DIM}  Last check : {ts}   |   Run #{run}{RESET}\n")

    # CPU
    print(f"  {WHITE}CPU Usage{RESET}")
    print(f"  {bar(m['cpu_pct'], CPU_WARN, CPU_CRIT)}  {BOLD}{m['cpu_pct']:5.1f}%{RESET}  {status_label(m['cpu_pct'], CPU_WARN, CPU_CRIT)}")
    print()

    # RAM
    print(f"  {WHITE}RAM Usage{RESET}  {DIM}({m['ram_used']} MB / {m['ram_total']} MB){RESET}")
    print(f"  {bar(m['ram_pct'], RAM_WARN, RAM_CRIT)}  {BOLD}{m['ram_pct']:5.1f}%{RESET}  {status_label(m['ram_pct'], RAM_WARN, RAM_CRIT)}")
    print()

    # DISK
    print(f"  {WHITE}Disk Usage{RESET} {DIM}({m['disk_used']} GB / {m['disk_total']} GB){RESET}")
    print(f"  {bar(m['disk_pct'], DISK_WARN, DISK_CRIT)}  {BOLD}{m['disk_pct']:5.1f}%{RESET}  {status_label(m['disk_pct'], DISK_WARN, DISK_CRIT)}")
    print()

    print(f"{DIM}  ─────────────────────────────────────────────{RESET}")
    print(f"  📁 Log  : {LOG_FILE}")
    print(f"  ⏱️  Interval: every {CHECK_INTERVAL}s  |  Ctrl+C to stop\n")

def main():
    print(f"{CYAN}Starting Health Monitor... Press Ctrl+C to quit.{RESET}")
    time.sleep(1)
    run = 0
    try:
        while True:
            run += 1
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            m  = get_metrics()
            display(m, ts, run)
            write_log(ts, m)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Monitor stopped. Log saved → {LOG_FILE}{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
