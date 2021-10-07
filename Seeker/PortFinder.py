import serial
def FindPort():
    try:
        ser = serial.Serial("/dev/ttyUSB0", '9600')
        print('Connected to USB0')
        return(ser)
    except:
        print('MATTWARE not connected USB0 ....')

    try:
        ser = serial.Serial("/dev/ttyUSB1", '9600')
        print('Connected to USB1')
        return(ser)
    except:
        print('MATTWARE not connected USB1....')

    try:
        ser = serial.Serial("/dev/ttyUSB2", '9600')
        print('Connected to USB2')
        return(ser)
    except:
        print('MATTWARE not connected USB2....')

    try:
        ser = serial.Serial("/dev/ttyUSB3", '9600')
        print('Connected to USB3')
        return(ser)
    except:
        print('MATTWARE not connected USB3....')

    try:
        ser = serial.Serial("/dev/ttyUSB4", '9600')
        print('Connected to USB4')
        return(ser)
    except:
        print('MATTWARE not connected USB4....')