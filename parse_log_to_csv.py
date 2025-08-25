import pandas as pd
import re

log_path = "/home/ahyeon/logs/test.log"
csv_path = "log_data.csv"

rows = []

with open(log_path, "r") as f:
    for line in f:
        timestamp_match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
        if timestamp_match:
            timestamp = timestamp_match.group(1)
            content = line[len(timestamp):].strip()
            rows.append({"timestamp": timestamp, "message": content})

df = pd.DataFrame(rows)
df.to_csv(csv_path, index=False)

print(f"✅ 로그를 CSV로 저장했습니다: {csv_path}")
