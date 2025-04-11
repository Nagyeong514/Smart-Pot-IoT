# 🌱 Smart Pot IoT (스마트 화분 프로젝트)

Raspberry Pi와 다양한 센서를 활용하여, **화분의 상태를 자동으로 감지하고 원격에서 제어할 수 있는 스마트 화분 시스템**입니다.  
웹 대시보드를 통해 실시간 센서 정보 확인 및 물 주기 제어가 가능합니다.

---

## ✅ 주요 기능

- 🌡️ 온도 / 💧 습도 / ☀️ 조도 실시간 측정
- 📷 화분 카메라 이미지 웹에 표시
- 💦 물 주기 버튼으로 릴레이 제어
- Flask 기반 웹 서버 구현
- 터치스크린 디스플레이 / 외부 접속 대응 가능

---

## 🛠 사용 기술

- Raspberry Pi 3B/4 + Raspbian OS
- Python 3
- Flask
- OpenCV (카메라 촬영)
- RPi.GPIO, Adafruit_DHT
- HTML / CSS (웹 UI)

---

## 🚀 설치 및 실행 방법

```bash
# 1. 패키지 설치
sudo apt update
sudo apt install python3-pip python3-smbus i2c-tools libcamera-apps -y
pip3 install flask opencv-python RPi.GPIO adafruit-circuitpython-dht

# 2. 인터페이스 활성화
sudo raspi-config
# → Interface Options: I2C, Camera 활성화 후 재부팅

# 3. 서버 실행
python3 app.py
# 브라우저에서 http://raspberrypi.local:5000 접속
