import modbus_tk.modbus_rtu as modbus_rtu
import serial
from modbus_tk import defines as cst
from modbus_tk import modbus
import time


def connect(baud):
    def decorator(func):
        def wrapper(port, *args, **kwargs):
            try:
                # Configure the serial port
                serial_port = serial.Serial(
                    port=port,      # Use the port passed to the decorator
                    baudrate=baud,  # Replace with your baud rate
                    bytesize=8,
                    parity='N',     # Parity: N=None, E=Even, O=Odd
                    stopbits=1,
                    timeout=1
                )
                client = modbus_rtu.RtuMaster(serial_port)
                client.set_timeout(1.0)
                client.set_verbose(True)
                # Inject the client into the function
                kwargs['client'] = client
                # Call the decorated function
                result = func(port, *args, **kwargs)
            except modbus.ModbusError as e:
                print(f"Modbus error: {e}")
                result = None
            except Exception as e:
                print(f"Error: {e}")
                result = None
            finally:
                # Close the Modbus connection
                client.close()
            return result
        return wrapper
    return decorator


@connect(baud=19200)
def read_temp(port, register=0x0100, client=None):
    try:
        # Read holding register (function code 03) from slave address 0x02
        response = client.execute(0x02, cst.READ_HOLDING_REGISTERS, register, 1)
        result = response[0]
        # print(f"Temperature: {temperature}°C")
        # print(f"result: {result}")
    except modbus.ModbusError as e:
        print(f"Modbus error: {e}")
        result = None
    except Exception as e:
        print(f"Error: {e}")
        result = None
    return result


@connect(baud=19200)
def write_temp(port, register, value, client=None):
    try:
        # Write single holding register (function code 06) to slave address 0x01
        client.execute(0x02, cst.WRITE_SINGLE_REGISTER, register, output_value=value)
        print(f"Successfully wrote {value} to register {hex(register)}")

    except modbus.ModbusError as e:
        print(f"Modbus error: {e}")
    except Exception as e:
        print(f"Error: {e}")


@connect(baud=9600)
def read_correction(port, register, client=None, max_retries=20, retry_delay=0.09):
    retries = 0
    result = None

    while retries < max_retries:
        try:
            # Read holding register (function code 03) from slave address 0x01
            response = client.execute(0x01, cst.READ_HOLDING_REGISTERS, register, 1)
            result = response[0]

            # Validate the result, if it's valid, return it
            if register == 0x021B:
                if result is not None and 700 <= result <= 1500:
                    return result
            elif register == 0x021C and (result > 2000 or result < 99):
                if result is not None:
                    return result
            else:
                pass
            # If result is invalid, log the attempt and retry
            print(f"Invalid result: {result}. Retrying...")


        except modbus.ModbusError as e:
            print(f"Modbus error: {e}. Retrying...")
            pass

        except Exception as e:
            print(f"Error: {e}. Retrying...")
            pass

        retries += 1
        retry_delay += 0.1
        time.sleep(retry_delay)

    # If maximum retries are reached, return None or handle it accordingly
    print("Maximum retries reached, unable to get valid response.")
    return None


@connect(baud=9600)
def write_correction(port, register, value, client=None, max_retries=10, retry_delay=0.08):
    retries = 0
    success = False

    while retries < max_retries and not success:
        try:
            # Write single holding register (function code 06) to slave address 0x01
            client.execute(0x01, cst.WRITE_SINGLE_REGISTER, register, output_value=value)
            # print(f"Successfully wrote {value} to register {hex(register)}")
            success = True  # Set flag to true if write was successful

        except modbus.ModbusError as e:
            # print(f"Modbus error: {e}. Retrying...")
            pass

        except Exception as e:
            # print(f"Error: {e}. Retrying...")
            pass

        retries += 1
        retry_delay += 0.1
        time.sleep(retry_delay)

    if not success:
        print(f"Failed to write {value} to register {hex(register)} after {max_retries} retries.")


if __name__ == '__main__':
    temp_port = "COM4"
    set_port = "COM10"
    read_temp(temp_port, 0x0100)
    # time.sleep(0.08)
    # write_correction(set_port, 0x021C, value=5)
    write_correction(set_port, 0x021B, value=990)
    time.sleep(0.08)
    read_correction(set_port, 0x021B)
    time.sleep(0.08)
    read_correction(set_port, 0x021C)

