import spidev # SPI 통신을 사용할 수 있게 하는 라이브러리 

spi = spidev.SpiDev() # SPI 객체 생성

spi.open(0,0) # SPI 통신 시작 

spi.max_speed_hz = 1000000 # SPI 통신속도 설정 (1MHz)

def analog_read(portChanner):
    adc = spi.xfer2([1, (8+portChanner)<<4, 0])
    data = ((adc[1]&3)<<8)+adc[2]
    
    return data