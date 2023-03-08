import time
from gpiozero import LED, InputDevice

led = LED(4)
led.on()
print("LED on!")
time.sleep(1)
led.off()
print("LED off!")

lsr = InputDevice(27)
start = time.time()
while (time.time() - start) < 10:
    print(str(lsr.value))
    if lsr.value < 1:
        print("light!")
        led.on()
    else:
        led.off()
