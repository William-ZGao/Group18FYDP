import time
from gpiozero import LED, InputDevice

led = LED(4)
lsr = InputDevice(27)
start = time.time()
led.on()
while (time.time() - start) < 5:
    if lsr.value < 1:
        print("light!")
print("========================================")
print("========================================")
print("========================================")
led.off()
while (time.time() - start) < 5:
    if lsr.value < 1:
        print("light!")