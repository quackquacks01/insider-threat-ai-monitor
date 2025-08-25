import os
import pandas as pd
from pycaret.anomaly import setup, create_model, assign_model, save_model

# Step 1: 로그 생성
log_dir = os.path.expanduser("~/logs")
log_file = os.path.join(log_dir, "test.log")
os.makedirs(log_dir, exist_ok=True)

if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("""\
2025-04-29 13:30:00 User login success
2025-04-29 09:10:00 email sent user=ahyeon to=teammate@example.com
2025-04-29 13:00:00 file open user=ahyeon file=report.docx
2025-04-29 03:20:00 external data transfer user=ahyeon size=1GB
2025-04-29 01:00:00 mass file copy user=ahyeon count=500
""")

# Step 2: 로그 → CSV
csv_file = "log_data.csv"
with open(log_file, "r") as f:
    lines = f.readlines()

df = pd.DataFrame({
    "timestamp": [line.split(" ", 2)[0] + " " + line.split(" ", 2)[1] for line in lines],
    "event": [line.split(" ", 2)[2].strip() for line in lines],
})
df.to_csv(csv_file, index=False)

# Step 3: PyCaret 이상탐지
exp = setup(data=df, session_id=42, silent=True, verbose=False)
model = create_model('iforest')
results = assign_model(model)

# 결과 출력
print(results.head())

# 모델 저장
save_model(model, 'iforest_model')
