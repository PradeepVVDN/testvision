import serial
import time
port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1, rtscts=False,
                     dsrdtr=False)
t_end = 10


def runclient(cmd):
    count = 0
    while count < 1:
        output = ""
        port.write(cmd.encode())
        count = 1
        if port:
            if port.in_waiting > 0 and count != 1:
                count = 1
                print("Test In progress", output)
                time.sleep(1)
                continue
            elif port.in_waiting == 0 and count == 1:
                break
        else:
            break


if __name__ == '__main__()':
    pass

