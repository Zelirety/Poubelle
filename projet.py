import pyfirmata as pf
import time

board = pf('COM5')

while True:
    board.digital[2].write(1)
    time.sleep(1)
    board.digital[2].write(0)
    time.sleep(1)
