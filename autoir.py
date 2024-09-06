import numpy as np


def get_order(current_temp, listx=list(range(280, 345, 5))):
    # Find the minimum and maximum values of the list
    min_value = min(listx)
    max_value = max(listx)
    distance_to_min = abs(current_temp - min_value)
    distance_to_max = abs(current_temp - max_value)

    if distance_to_min < distance_to_max:
        return listx
    elif distance_to_max < distance_to_min:
        return listx[::-1]
    else:
        return listx


def get_ir_correction(dicty, slope, intercept):
    span = 1-slope
    offset = 0
    return span, offset



current_temp = 100
order = get_order(current_temp)

listx = list(range(280, 345, 5))
listy = [280.9, 284.8, 291.2, 295.3, 300, 305,
         310.2, 315.1, 320.3, 325.6, 329, 334, 341]
slope, intercept = np.polyfit(listx, listy, 1)

print(order)
