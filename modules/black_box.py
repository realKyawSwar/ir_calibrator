
import serial


def calculate_lrc(command_bytes):
    lrc = 0
    for byte in command_bytes:
        lrc = (lrc + byte) & 0xFF
    lrc = ((~lrc + 1) & 0xFF)  # Two's complement
    return lrc


def construct_command(cmd0, data_address, data):
    # Define the fields
    stx = ':'
    adr0 = 0x01
    # Create the command bytes
    command_bytes = [adr0, cmd0,
        (data_address >> 8) & 0xFF,  # High byte of data_address
        data_address & 0xFF,         # Low byte of data_address
        (data >> 8) & 0xFF,         # High byte of data
        data & 0xFF                 # Low byte of data
    ]

    # Calculate the LRC
    lrc = calculate_lrc(command_bytes)
    lrc_high = (lrc >> 4) & 0x0F
    lrc_low = lrc & 0x0F
    # Convert to hex characters
    lrc_high_char = format(lrc_high, 'X')
    lrc_low_char = format(lrc_low, 'X')
    command_string = f"{stx}{adr0:02X}{cmd0:02X}{data_address:04X}{data:04X}{lrc_high_char}{lrc_low_char}\r\n"
    return command_string



def extract_and_decode(reply):
    """
    Extracts hexadecimal values from the given reply string and converts them to decimal.

    Parameters:
    reply (str): A string containing the serial reply.

    Returns:
    dict: A dictionary with the start addresses and their corresponding decimal values.
    """
    # Extract the content of the start addresses from the reply string
    hex_4700H = reply[7:11]
    hex_4701H = reply[11:15]

    # Convert hexadecimal to decimal
    decimal_4700H = int(hex_4700H, 16)/10
    decimal_4701H = int(hex_4701H, 16)/10

    return {
        '4700H': decimal_4700H,
        '4701H': decimal_4701H
    }


def send_and_receive(serial_port, command):
    with serial.Serial(serial_port,
                       baudrate=9600,
                       bytesize=serial.SEVENBITS,
                       parity=serial.PARITY_EVEN,
                       stopbits=serial.STOPBITS_ONE,
                       timeout=1) as ser:
        ser.write(command.encode())
        reply = ser.readline()
        return reply


def read_temp(com):
    cmd0 = 0x03
    data_address = 0x4700
    data = 0x0002
    read_cmd = construct_command(cmd0, data_address, data)
    # reply = ":01030400E503E828"
    reply = send_and_receive(com, read_cmd)
    # print("Received reply:", reply)
    # Extract and decode the content
    decoded_values = extract_and_decode(reply)
    # Print the results
    # print(f"Content of start address 4700H (hex: {reply[9:13]}) is {decoded_values['4700H']} in decimal.")
    # print(f"Content of start address 4701H (hex: {reply[13:17]}) is {decoded_values['4701H']} in decimal.")
    return decoded_values['4700H'], decoded_values['4701H']


def set_temp(com, number):
    number_str = str(number)
    # Append '0' to the string
    result_str = number_str + '0'
    # Convert the result back to an integer
    temp= int(result_str)
    # cmd1 = 0x00
    cmd0 = 0x06
    data_address = 0x4701
    data = int(hex(temp), 16)
    write_cmd = construct_command(cmd0, data_address, data)
    reply = send_and_receive(com, write_cmd).decode()
    if reply == write_cmd:
        print("success")
    else:
        print("failed")


if __name__ == '__main__':
    com = "COM9"
    readback, setting = read_temp(com)
    print(readback, setting)
    # set_temp(com, 23)
