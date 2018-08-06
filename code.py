from adafruit_circuitplayground.express import cpx
import time
off = (0, 0, 0) 

while True:
    cpx.pixels.brightness = 0.5
    cpx.pixels.fill ((155, 5, 80))
    time.sleep (0.2)
    cpx.pixels.brightness = 0.5
    cpx.pixels.fill ((0, 0, 0))
    time.sleep (0.2)
    
    