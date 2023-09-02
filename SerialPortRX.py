import serial

# Define the serial port and baud rate
ser = serial.Serial("/dev/serial1", 115200)

while True :
    try:
    
        #Receiving data
        received_data = ser.read()  # Read a line from the serial port
        decoded_data = received_data # Decode bytes to string and remove newline characters

        print(f"Received: {decoded_data}")
        #sleep(0.03)

    except serial.SerialException as e:
        print(f"Serial Exception: {e}")
