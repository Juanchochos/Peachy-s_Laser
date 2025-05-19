from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servo = Servo(23, pin_factory=factory)
servo2 = Servo(24, pin_factory=factory)

print("Testing servo positions")

try:
    while True:
        print("Min")
        servo.min()
        servo2.min()
        sleep(1)
              
        print("Mid")
        servo.mid()
        servo2.mid()
        sleep(1)

        print("Max")
        servo.max()
        servo2.max()
        sleep(1)      

except KeyboardInterrupt:
    print("Test interrupted, exiting...")

