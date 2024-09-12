from time import sleep
import random
from modules import ir_sensor, controller, notify, logs
# from modules import controller

def initialize_ir(temp_port, set_port):
    span = ir_sensor.read_correction(set_port, 0x021B)
    sleep(0.08)
    sleep(1)
    zero = ir_sensor.read_correction(set_port, 0x021C)
    delay = 0.08
    while span != 1000:
        # sleep(0.1)
        ir_sensor.write_correction(set_port, 0x021B, value=1000)
        sleep(delay)
        span = ir_sensor.read_correction(set_port, 0x021B)
        sleep(delay)
        delay += 0.1
    delay = 0.08
    while zero != 0:
        ir_sensor.write_correction(set_port, 0x021C, value=0)
        sleep(delay)
        zero = ir_sensor.read_correction(set_port, 0x021C)
        sleep(delay)
    print(span, zero)
    original_emiss = ir_sensor.read_temp(temp_port, 0x0103)
    sleep(4)
    if original_emiss != 950:
        sleep(0.08)
        ir_sensor.write_temp(temp_port, 0x0103, value=950)
        sleep(0.08)
        ir_sensor.read_temp(temp_port, 0x0103)
    print(span)
    print(zero)
    print(original_emiss)
    return original_emiss


def send_msg(data, serial_number, sesp, signed_value):

    table = f"This {serial_number} ir sensor is completed.\n"
    # Convert the dictionary to a formatted string table
    table += "Try      | Slope | Intercept\n" + "-"*32 + "\n"
    for key, values in data.items():
        table += f"{key:<10} | {values[0]:<7} | {values[1]:<7}\n"
    table += f"SESP is {sesp} and SEOF is {signed_value}"
    # Print or send the table string as a message
    # print(table)
    logs.logInfo(table)
    try:
        notify.trigger_notify(table, "8208595182569485")
        # test
        # trigger_notify(table, "5677283929052213")
    except Exception as err:
        logs.logError(f"{err} at workchat",
                      includeErrorLine=True)


if __name__ == "__main__":
    bb_port = "COM14"
    temp_port = "COM4"
    set_port = "COM13"
    logs.initLogger("auto_ir")
    control = controller.TemperatureController(bb_port)
    try:
        original_emiss = initialize_ir(temp_port, set_port)
        slopey, inty, dicty = controller.slope_routine(control, bb_port, temp_port, set_port)
        data= controller.intercept_routine(control, bb_port, temp_port, set_port, slopey, inty, dicty)
        seof = ir_sensor.read_correction(set_port, 0x021C)
        signed_value = controller.to_signed(seof)
        sleep(5)
        sesp = round(ir_sensor.read_correction(set_port, 0x021B) / 1000)
        serial_number = 'test'
        send_msg(data, serial_number, sesp, signed_value)
    except Exception as e:
        logs.logError(e, includeErrorLine=True)

    finally:
        logs.closeLogger()
    control.set_temperature(300)

    # print(sesp)
