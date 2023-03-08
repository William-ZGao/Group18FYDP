import time
from gpiozero import LED, LightSensor

led = LED(4)
led.on()
print("LED on!")
time.sleep(1)
led.off()
print("LED off!")

lsr = LightSensor(27)
start = time.time()
while (time.time() - start) > 10:
    bright = lsr.value
    print(str(bright))
    if bright == 1:
        led.on()
    else:
        led.off()