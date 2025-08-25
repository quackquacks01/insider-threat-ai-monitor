# insider-threat-ai-monitor 🔒🤖
생성형 AI 기반 내부자 행위 선제 감시 체계  

---

## 📑 프로젝트 개요
- **실험 환경**: Ubuntu Server 22.04, 가상 내부망 환경, CERT Insider Threat Dataset 일부 활용  
- **데이터 종류**: 인증 로그, 파일 접근 로그, 네트워크 통신, 이메일 송수신, 명령어 실행 기록  
- **핵심 목표**
  - 내부자 위협(Insider Threat) 조기 탐지 및 실시간 경고
  - PyCaret 기반 이상 탐지 모델 + Generative AI 요약 결합
  - Streamlit 대시보드 기반 실시간 모니터링/대응

---

## 📂 Repository 구조
```markdown
insider_threat/
│
├── auto_log_analysis.py # PyCaret 기반 로그 자동 분석 (Anomaly Score 계산)
├── log_dashboard.py # Streamlit 대시보드 UI
├── parse_log_to_csv.py # 로그 파일 → CSV 변환기
├── log_data.csv # 샘플 로그 데이터
└── README.md
```


---

## ⚙️ **주요 기능**
- **데이터 수집/전처리**
  - Apache NiFi + Filebeat + Logstash 기반 로그 파이프라인
  - 로그 정규화, 익명화, 타임스탬프 동기화
- **정상 행동 프로파일링**
  - K-Means 클러스터링 기반 사용자 프로파일
  - LLM(LLaMA2/GPT-2) 기반 일일 행동 요약
- **이상 탐지/경고**
  - PyCaret Anomaly Detection (Z-Score, Isolation Forest)
  - 이상 징후 자연어 요약 → 관리자가 직관적으로 이해 가능
  - Risk Score 기반 단계별 대응 정책 (≥70 경고, ≥90 차단)
- **시각화/자동화**
  - Streamlit 대시보드: 위험 사용자 Top-5, Score 분포, 대응 버튼
  - Kibana 연동 시각화 지원
  - 자동 PDF 리포트 생성 기능

---

## 🏆 주요 성과
- 테스트 시나리오 4건 중 3건 탐지 성공 → **탐지율 75%**
- **오탐율 0%**, 탐지 후 평균 **2분 이내 경고 발송**
- 위험 Score 기반 실시간 평가 (시나리오별 75~90점)
- 탐지 → 요약 → 경고 → 대응까지 **엔드투엔드 대응 체계 구현**
- 관리자의 상황 인지 속도 평균 **30% 이상 단축**
- 공공기관/국가기반시설 적용 가능성 검증

---

## 🔧 기술 스택
- **언어/라이브러리**: Python, PyCaret, scikit-learn, pandas  
- **AI 모델**: LLaMA2, GPT-2 (보안 행동 데이터셋 기반 파인튜닝)  
- **로그 파이프라인**: Apache NiFi, Filebeat, Logstash, Elasticsearch  
- **시각화/운영**: Streamlit, Kibana, ReportLab  
- **인프라**: Ubuntu Server 22.04, AWS S3 + Glue Catalog  

---

## 🚀 실행 방법
```bash
# 로그 데이터 CSV 변환
python parse_log_to_csv.py

# 이상 탐지 자동 실행 (PyCaret 기반)
python auto_log_analysis.py

# 실시간 대시보드 실행
streamlit run log_dashboard.py
```

---

## 📜 License
```text
MIT License

Copyright (c) 2025 quackquacks01

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
