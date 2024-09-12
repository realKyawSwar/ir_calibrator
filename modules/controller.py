from time import sleep
from modules.black_box import read_temp, set_temp
from modules import ir_sensor, notify
# import ir_sensor
import numpy as np
import time

class TemperatureController:
    def __init__(self, com_port):
        self.com_port = com_port

    def set_temperature(self, temperature):
        set_temp(self.com_port, temperature)

    def get_temperature(self):
        return read_temp(self.com_port)


def timer_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"took {elapsed_time:.4f} seconds to complete.")
        return result
    return wrapper


# def wait_until_temp_reached(controller, set_temp):
#     while True:
#         current_temp, _ = controller.get_temperature()
#         if current_temp == set_temp:
#             break
#         print(f"Waiting for current temperature to reach {set_temp}°C...")
#         sleep(60)
@timer_function
def wait_until_temp_reached(controller, set_temp):
    while True:
        current_temp, _ = controller.get_temperature()
        if current_temp == set_temp:
            break

        # Calculate the temperature difference
        temp_diff = abs(current_temp - set_temp)

        # Adjust sleep time based on the temperature difference
        if temp_diff > 3:
            wait_time = 60  # Wait for 60 seconds if the difference is large
        elif temp_diff > 2:
            wait_time = 45  # Wait for 30 seconds if the difference is moderate
        elif 0.2 < temp_diff < 1:
            wait_time = 25  # Wait for 30 seconds if the difference is moderate
        else:
            wait_time = 10  # Wait for 10 seconds if the difference is small

        print(f"Waiting for current temperature ({current_temp}°C) to reach {set_temp}°C... Sleeping for {wait_time} seconds.")
        sleep(wait_time)



def send_slope(data):

    data = f"setting slope {data}.\n"
    try:
        notify.trigger_notify(data, "8208595182569485")
        # test
        # trigger_notify(table, "5677283929052213")
    except Exception as err:
        # logs.logError(f"{err} at workchat",
        #               includeErrorLine=True)
        print(f"send slope error: {err}")


def get_order(controller, listx=list(range(300, 306, 1))):
    # Find the minimum and maximum values of the list
    current_temp, _ = controller.get_temperature()
    distance_to_min = abs(current_temp - min(listx))
    distance_to_max = abs(current_temp - max(listx))
    if distance_to_min < distance_to_max:
        return listx
    elif distance_to_max < distance_to_min:
        return listx[::-1]
    else:
        return listx


def get_slope(controller, bb_port, temp_port, set_port):
    bb_temperature = controller.get_temperature()
    print(f"Black box is {bb_temperature}")
    listx = get_order(controller)
    print(listx)
    listy = []
    for target_temp in listx:
        print(f"Setting temperature to {target_temp}°C...")
        controller.set_temperature(target_temp)
        # Wait until current temperature matches set temperature
        wait_until_temp_reached(controller, target_temp)
        # Wait for 3 minutes
        # print("Waiting for 1 minutes...")
        # sleep(60)
        ir_temperature = ir_sensor.read_temp(temp_port, 0x0100) / 10
        print(ir_temperature)
        listy.append(ir_temperature)
    slope, intercept = np.polyfit(listx, listy, 1)
    return slope, intercept


def slope_routine(controller, bb_port, temp_port, set_port):
    # Get the initial slope and intercept
    slope, intercept = get_slope(controller, bb_port, temp_port, set_port)
    dicty = {'initial': (slope, intercept)}
    original_slope = 1
    # Initialize span_input and old_slope
    span_input = original_slope - (slope - 1)
    tries = 1  # Initialize the tries counter
    # Continue adjusting until slope is within range
    while not 0.995 <= slope <= 1.005:
        # Calculate the sensor correction value
        sesp = round(span_input * 1000)
        delay = 0.08
        span = ir_sensor.read_correction(set_port, 0x021B)
        while sesp != span:
            sleep(delay)
            ir_sensor.write_correction(set_port, 0x021B, value=sesp)
            sleep(delay)
            span = ir_sensor.read_correction(set_port, 0x021B)
            delay += 0.1

        # Update the slope and intercept after adjustment
        slope, intercept = get_slope(controller, bb_port, temp_port, set_port)
        # Log the new values in the dictionary
        dicty[f'try_{tries}'] = (slope, intercept)
        # Update span_input for the next iteration
        span_input = (sesp/1000) - (slope - 1)
        send_slope(span_input)
        # Increment tries counter
        tries += 1
    print("Slope is now within the range:", slope)
    print("All recorded slope and intercept values:", dicty)
    return slope, intercept, dicty


def to_signed(value: int):
    if value >= 32768:
        value -= 65536
    return value/10


def to_unsigned(value):
    if value < 0:
        value += 65536  # Convert negative to two's complement
    return value


def intercept_routine(controller, bb_port, temp_port, set_port, slope, intercept, dicty):
    # Initialize span_input and old_slope
    original_intercept = 0
    offset_input =  original_intercept - intercept

    tries = len(dicty)
    # Continue adjusting until slope intercept is within range
    while not (-1 <= intercept <= 1) and (0.995 <= slope <= 1.005):
        if not -1 <= intercept <= 1:
            # Calculate the sensor correction value
            # seof = round(offset_input * 1000)
            unsigned_offset = round(to_unsigned(offset_input))
            delay = 0.08
            offset = ir_sensor.read_correction(set_port, 0x021C)
            while unsigned_offset != offset:
                sleep(delay)
                ir_sensor.write_correction(set_port, 0x021C, value=unsigned_offset)
                sleep(delay)
                offset = ir_sensor.read_correction(set_port, 0x021C)
                delay += 0.1

        sleep(5)

        if not 0.995 <= slope <= 1.005:
            present_slope = ir_sensor.read_correction(set_port, 0x021B)
            dummy_sp = present_slope / 1000
            span_input = dummy_sp - (slope - 1)
            sesp = round(span_input * 1000)
            delay = 0.08
            span = ir_sensor.read_correction(set_port, 0x021B)
            while sesp != span:
                sleep(delay)
                ir_sensor.write_correction(set_port, 0x021B, value=sesp)
                sleep(delay)
                span = ir_sensor.read_correction(set_port, 0x021B)
                delay += 0.1

        # Update the slope and intercept after adjustment
        slope, intercept = get_slope(controller, bb_port, temp_port, set_port)
        dicty[f'try_{tries}'] = (slope, intercept)
        # Update span_input for the next iteration
        # check negative here!
        seof = ir_sensor.read_correction(set_port, 0x021C)
        signed_seof = to_signed(seof)
        offset_input = signed_seof - intercept
        # Increment tries counter
        tries += 1
    print("intercept is now within the range:", intercept)
    print("All recorded slope and intercept values:", dicty)
    return dicty


if __name__ == "__main__":
    bb_port = "COM14"
    temp_port = "COM4"
    set_port = "COM13"
    controller = TemperatureController(bb_port)
    # slopey, inty, dicty = slope_routine(controller, bb_port, temp_port, set_port)
    # new_dicty = intercept_routine(controller, bb_port, temp_port, set_port, slopey, inty, dicty)
    # print(new_dicty)
    seof = ir_sensor.read_correction(set_port, 0x021C)
    signed_value = to_signed(seof)
    print(signed_value)
