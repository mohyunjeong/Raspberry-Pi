import picamera as pc # 카메라 불러오기 
import time

camera = pc.PiCamera()  

camera.start_preview() # 화면 열기 
time.sleep(5)

for i in range(3) : 
    camera.capture(f'image{i}.jpg') # 사진 저장
    time.sleep(1)
    
camera.stop_preview() # 화면 닫기 

camera.close() # 카메라 닫기
