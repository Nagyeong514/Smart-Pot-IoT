# sudo apt install libcamera-apps
# pip3 install opencv-python

# 역할: 카메라로 이미지 촬영 → static/cam.jpg로 저장


import cv2

def capture_image():
    cap = cv2.VideoCapture(0)  # Pi Camera 또는 USB 카메라
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('static/cam.jpg', frame)  # 이미지 저장
    cap.release()
