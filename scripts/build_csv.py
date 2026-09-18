import os
import json
import csv
from pathlib import Path

LOG_DIR = "logs"
OUTPUT_FILE = "reports/line_message_log.csv"

records = []

for file in sorted(Path(LOG_DIR).glob("*.json")):
    try:
        with open(file, "r", encoding="utf-8") as f:

            data = json.load(f)

            records.append({
                "EventId": data.get("EventId", ""),
                "MessageId": data.get("MessageId", ""),
                "Timestamp": data.get("Timestamp", ""),
                "ReceivedTime": data.get("ReceivedTime", ""),
                "SourceType": data.get("SourceType", ""),
                "GroupId": data.get("GroupId", ""),
                "RoomId": data.get("RoomId", ""),
                "UserId": data.get("UserId", ""),
                "MessageType": data.get("MessageType", ""),
                "MessageText": str(data.get("MessageText", "")).replace("\r\n", " ").replace("\n", " "),
                "IsRedelivery": data.get("IsRedelivery", False)
            })

    except Exception as ex:
        print(f"Skip {file}: {ex}")

records.sort(
    key=lambda x: x["Timestamp"]
)

os.makedirs(
    "reports",
    exist_ok=True
)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8-sig",
    newline=""
) as csvfile:

    fieldnames = [
        "EventId",
        "MessageId",
        "Timestamp",
        "ReceivedTime",
        "SourceType",
        "GroupId",
        "RoomId",
        "UserId",
        "MessageType",
        "MessageText",
        "IsRedelivery"
    ]

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(records)

print(f"CSV generated: {OUTPUT_FILE}")
