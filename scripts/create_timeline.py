
import csv
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
OUTPUT = ROOT / "timeline" / "attack_timeline.csv"

events = []

# Read system logs
system_file = EVIDENCE / "system_logs.txt"

with open(system_file, encoding="utf-8") as f:
    for line in f:
        match = re.search(
            r"(\d{2}:\d{2}:\d{2})\s*-\s*(.*)",
            line
        )
        if match:
            timestamp = datetime.strptime(
                "18-11-2026 " + match.group(1),
                "%d-%m-%Y %H:%M:%S"
            )
            events.append([
                timestamp, match.group(2), "System Logs"
            ])

# Read login and network CSV files
for filename in ["login_records.csv", "network_logs.csv"]:
    with open(EVIDENCE / filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            timestamp = datetime.strptime(
                row["Timestamp"], "%d-%m-%Y %H:%M"
            )
            events.append([
                timestamp,
                str(row),
                filename
            ])

events.sort(key=lambda x: x[0])

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Event", "Source"])
    for event in events:
        writer.writerow([
            event[0].strftime("%d-%m-%Y %H:%M:%S"),
            event[1],
            event[2]
        ])

print("Attack timeline generated successfully.")
print("Output:", OUTPUT)
print("Total events:", len(events))
