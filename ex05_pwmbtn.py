# 버튼 눌러서 led 밝기 단계 제어하기

import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(21, gp.IN)
gp.setup(18, gp.OUT)

p = gp.PWM(18, 500)
p.start(0)

cnt = 0
state = True

try :
    while True :
        btn = gp.input(21)
        if (btn == 1) :
            if (state == True) :
                cnt += 1
                state = False
        elif (btn == 0) :
            state = True
            
#         if (cnt == 1) :
#             p.ChangeDutyCycle(20)
#         elif (cnt == 2) :
#             p.ChangeDutyCycle(50)
#         elif (cnt == 3) :
#             p.ChangeDutyCycle(100)
#         else :
#             p.ChangeDutyCycle(0)
#             cnt = 0

        if cnt % 3 == 0 :
            p.ChangeDutyCycle(20)
        elif cnt % 3 == 1 :
            p.ChangeDutyCycle(50)
        else :
            p.ChangeDutyCycle(100)
        
except KeyboardInterrupt :
    gp.cleanup()
