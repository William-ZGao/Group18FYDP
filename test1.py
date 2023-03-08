import time
from gpiozero import LED, DigitalInputDevice

led = LED(4)
led.on()
print("LED on!")
time.sleep(1)
led.off()
print("LED off!")

lsr = DigitalInputDevice(27)
start = time.time()
while (time.time() - start) < 10:
    print(str(lsr.value))
    if lsr.value > 0:
        print("light!")
        led.on()
    else:
        led.off()
