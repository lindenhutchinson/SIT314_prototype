import serial
import time

ser = serial.Serial('COM3') # COMxx  format on Windows
ser.baudrate = 9600  # set Baud rate to 9600

write_to_file_path = 'moisture_data_serial.csv'
output_file = open(write_to_file_path, 'w+')
while True:
    line = ser.readline()
    line = line.decode('utf-8')
    if line:
        output_file.write(line)