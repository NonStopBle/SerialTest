import serial

# Define the serial port and baud rate
ser = serial.Serial("/dev/serial1", 115200)

while True :
    try:
        # Sending data
        data_to_send = "Hello, Serial!"
        ser.write(data_to_send.encode())  # Encode the string to bytes before sending

        # Receiving data
        #received_data = ser.readline()  # Read a line from the serial port
        #decoded_data = received_data.decode().strip()  # Decode bytes to string and remove newline characters

     #   print(f"Received: {decoded_data}")
        #sleep(0.03)

    except serial.SerialException as e:
        print(f"Serial Exception: {e}")
