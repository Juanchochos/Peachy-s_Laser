import curses
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# Set up pigpio factory and servos
factory = PiGPIOFactory()
servo_pan = Servo(17, pin_factory=factory)
servo_tilt = Servo(18, pin_factory=factory)

# Servo positions go from -1 (min) to 1 (max)
pan_pos = 0.0
tilt_pos = 0.0
step = 0.1  # how much to move per key press

def clamp(value, min_value=-1, max_value=1):
    return max(min(value, max_value), min_value)

def main(stdscr):
    global pan_pos, tilt_pos

    stdscr.nodelay(True)  # Don't block waiting for input
    stdscr.clear()
    stdscr.addstr(0, 0, "Use arrow keys to move servo. Press 'q' to quit.")

    while True:
        try:
            key = stdscr.getch()

            if key == curses.KEY_UP:
                tilt_pos = clamp(tilt_pos + step)
            elif key == curses.KEY_DOWN:
                tilt_pos = clamp(tilt_pos - step)
            elif key == curses.KEY_RIGHT:
                pan_pos = clamp(pan_pos + step)
            elif key == curses.KEY_LEFT:
                pan_pos = clamp(pan_pos - step)
            elif key == ord('q'):
                break

            # Move servos
            servo_pan.value = pan_pos
            servo_tilt.value = tilt_pos

            # Display current positions
            stdscr.addstr(2, 0, f"Pan position : {pan_pos:.2f}   ")
            stdscr.addstr(3, 0, f"Tilt position: {tilt_pos:.2f}   ")
            stdscr.refresh()

            time.sleep(0.05)

        except KeyboardInterrupt:
            break

curses.wrapper(main)

# Reset servos on exit
servo_pan.detach()
servo_tilt.detach()


