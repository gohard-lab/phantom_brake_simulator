# 🚗 Phantom Brake Simulator

자율주행 자동차의 다중 센서 환경(Sensor Fusion)에서 발생하는 데이터 충돌과 **'팬텀 브레이크(Phantom Braking)'** 현상을 파이썬으로 구현한 시뮬레이션 프로젝트입니다.

## 📌 프로젝트 소개
자율주행의 교과서적인 이론에서는 카메라, 레이더, 라이다 등 다양한 센서를 융합할수록 안전성이 높아진다고 설명합니다. 하지만 실제 주행 환경에서는 전파 난반사(Multipath Effect)나 기상 악화로 인해 센서 간의 판단(신뢰도)이 충돌하는 엣지 케이스가 발생합니다.

이 프로젝트는 레거시 자동차 브랜드들이 이러한 데이터 충돌 상황에서 어떻게 보수적인 **페일 세이프(Fail-Safe)** 로직을 작동시켜 불필요한 급제동을 유발하는지 논리적으로 모델링하고 분석합니다.

## ⚙️ 주요 기능 (Features)
* `camera_vision`: 광학 센서(카메라)의 전방 도로 상황 인식 시뮬레이션
* `radar_signal`: 전파 센서(레이더)의 장애물 감지 및 오탐지(False Positive) 난수 생성
* `fail_safe_logic`: 센서 간 데이터 불일치 발생 시 작동하는 긴급 제동 알고리즘

## 🛠 기술 스택 및 의존성 (Dependencies)
이 프로젝트는 최신 파이썬 생태계의 표준 패키지 관리 방식인 `pyproject.toml`을 사용합니다.

* **Language:** Python 3.10+
* **Data Visualization:** Plotly (시뮬레이션 로그 시각화용)

## 🚀 설치 및 실행 방법 (Installation & Usage)

1. 리포지토리를 클론합니다.
```bash
git clone [https://github.com/gohard-lab/phantom_brake_simulator.git](https://github.com/gohard-lab/phantom_brake_simulator.git)
cd phantom_brake_simulator
```

2. 패키지 의존성을 설치합니다.
```Bash
pip install .
```

3. 시뮬레이터를 실행합니다.
```Bash
python phantom_brake_simulator.py
```

📺 관련 유튜브 콘텐츠
이 코드에 대한 상세한 알고리즘 분석과, 이러한 하드웨어 센서의 딜레마를 '비전 AI'와 '엔드투엔드(End-to-End) 신경망'으로 극복하려는 테슬라의 기술적 접근 방식은 아래 유튜브 영상에서 확인하실 수 있습니다.

YouTube 채널: https://www.youtube.com/@PolymathDev_KR

상세 분석 영상: [유튜브 영상 링크 삽입 예정]