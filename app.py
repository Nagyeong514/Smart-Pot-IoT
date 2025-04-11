from flask import Flask, render_template, request, redirect
import random
import RPi.GPIO as GPIO
import time
from camera_capture import capture_image  # 카메라 함수 가져오기

app = Flask(__name__)

PUMP_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.LOW)

@app.route('/')
def index():
    capture_image()  # 페이지 접속할 때마다 사진 갱신

    temperature = round(random.uniform(20, 30), 1)
    humidity = round(random.uniform(40, 70), 1)
    light = random.randint(100, 800)

    return render_template('index.html', temp=temperature, humid=humidity, light=light)

@app.route('/pump', methods=['POST'])
def pump():
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(PUMP_PIN, GPIO.LOW)
    return redirect('/')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()



# 서버 실행 : python3 app.py
# http://raspberrypi.local:5000
# 또는 http://<라즈베리파이_IP>:5000
