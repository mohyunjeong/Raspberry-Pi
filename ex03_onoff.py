# 버튼 한번 눌렀을 때 led 켜고 한번 더 눌렀을 때 led 끄기

import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(21, gp.IN)
gp.setup(18, gp.OUT)

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
#             gp.output(18, gp.HIGH)
#         elif (cnt == 2) :
#             gp.output(18, gp.LOW)
#             cnt = 0

#         if cnt % 2 == 1 :
#             gp.output(18, 1)
#         else :
#             gp.output(18, 0)

        gp.output(18, cnt % 2)
        
except KeyboardInterrupt :
    gp.cleanup()
