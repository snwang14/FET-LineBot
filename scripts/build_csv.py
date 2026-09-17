import os
import json
import csv
from pathlib import Path

LOG_DIR = "logs"
OUTPUT_FILE = "reports/line_message_log.csv"

records = []

for file in sorted(Path(LOG_DIR).glob("*.json")):

    try:

        with *pen(
            file,
           *"r",
            encoding="utf-8"
*       ) as f:

            data =*json.load(f)

            records.*ppend({

                "EventId"*
                    data.get("Eve*tId", ""),

                "Messa*eId":
                    data.get*"MessageId", ""),

               *"Timestamp":
                    d*ta.get("Timestamp", ""),

        *       "ReceivedTime":
           *        data.get("ReceivedTime", "*),

                "SourceType":
*                   data.get("Sourc*Type", ""),

                "Grou*Id":
                    data.get(*GroupId", ""),

                "R*omId":
                    data.ge*("RoomId", ""),

                "*serId":
                    data.g*t("UserId", ""),

                *MessageType":
                    *ata.get("MessageType", ""),

     *          "MessageText":
         *          data.get("MessageText", *"),

                "IsRedelivery*:
                    data.get("Is*edelivery", False)

            })*
    except Exception as ex:

    *   print(f"Skip {file}: {ex}")

re*ords.sort(
    key=lambda x:
    x*"Timestamp"]
)

os.makedirs(
    "*eports",
    exist_ok=True
)

with*open(
    OUTPUT_FILE,
    "w",
  * encoding="utf-8-sig",
    newline*""
) as csvfile:

    fieldnames =*[

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

  * writer = csv.DictWriter(
        *svfile,
        fieldnames=fieldna*es
    )

    writer.writeheader()*
    writer.writerows(records)

pr*nt(
    f"CSV generated: {OUTPUT_F*LE}"
)
