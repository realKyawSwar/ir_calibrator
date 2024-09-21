from time import sleep
import random
from modules import ir_sensor, controller, notify, logs


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
    logs.logInfo(table)
    try:
        notify.trigger_notify(table, "8208595182569485")
    except Exception as err:
        logs.logError(f"{err} at workchat",
                      includeErrorLine=True)


if __name__ == "__main__":
    bb_port = "COM14"
    temp_port = "COM4"
    set_port = "COM13"
    control = controller.TemperatureController(bb_port)
    logs.initLogger("auto_ir")

    try:
        # original_emiss = initialize_ir(temp_port, set_port)
        # slopey, inty, dicty, dfs = controller.slope_routine(control, temp_port, set_port)

        dicty = {
                 'initial': (1.0453846153846156, -6.907692307692686),
                 'try_1': (1.0307692307692304, -7.500000000000079),
                 'try_2': (1.0198901098901079, -7.712087912087349),
                 'try_3': (1.005824175824174, -5.751648351647952),
                 'try_4': (1.0037362637362635, -5.865934065934165)
                 }
        slopey = 1.0037362637362635
        inty = -5.865934065934165
        dfs = []

        data, df_list = controller.intercept_routine(control, temp_port, set_port, 
                                                     slopey, inty, dicty, dfs)
        final_df = pd.concat(df_list, ignore_index=True)
        # Saving the final concatenated DataFrame to a CSV file
        final_df.to_csv('concatenated_dataframe.csv', index=False)

        seof = None
        delay = 0.08
        while not seof:
            seof = ir_sensor.read_correction(set_port, 0x021C)
            sleep(delay)
            delay += 0.1

        signed_value = controller.to_signed(seof)
        sleep(5)
        delay = 0.08
        sesp = None
        while not sesp:
            sesp = round(ir_sensor.read_correction(set_port, 0x021B) / 1000)
            sleep(delay)
            delay += 0.1
        serial_number = 'test'
        send_msg(data, serial_number, sesp, signed_value)
    except Exception as e:
        logs.logError(e, includeErrorLine=True)

    finally:
        logs.closeLogger()

    control.set_temperature(30)
