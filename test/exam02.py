import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(20, gp.IN)
gp.setup(21, gp.IN)
gp.setup(18, gp.OUT)

p = gp.PWM(18, 500)
p.start(0)

try :
    while True :
        btn1 = gp.input(20)
        btn2 = gp.input(21)
        if (btn1 == 1) :
            p.ChangeDutyCycle(50)
        elif (btn2 == 1) :
            p.ChangeDutyCycle(100)
        else :
            p.ChangeDutyCycle(0)
        
except KeyboardInterrupt :
    gp.cleanup()