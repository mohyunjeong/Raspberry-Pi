import picamera as pc

with pc.PiCamera() as camera : # camera = pc.Picamera()와 동일! 하지만 close를 사용하지 않아도 됨!
    
    camera.resolution = (640, 480) # 카메라 해상도 지정 
    
    camera.start_preview() # 카메라 열기 
    camera.start_recording('video.h264') # 동영상 저장 
    camera.wait_recording(5) # 초 단위로 지정 
    
    camera.stop_recording() # 저장 멈추기 
    camera.stop_preview() # 프리뷰 닫기 
    