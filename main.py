
def calculate_wind_power_3_6(wind_speed):
    """Calculate wind power 3.6 based on passing parameters"""

    wind_power_3_6 = 0
    if wind_speed < 2.75:
        wind_power_3_6 = 0

    elif 2.75 <= wind_speed < 4:
        wind_power_3_6 = 38594.4795 * wind_speed ** 2 + -91774.18866 * wind_speed + -6930.505107

    elif 4 <= wind_speed < 5:
        wind_power_3_6 = 50328.66804 * wind_speed ** 2 + -179633.9254 * wind_speed + 156761.425

    elif 5 <= wind_speed < 6:
        wind_power_3_6 = 70574.72694 * wind_speed ** 2 + -368403.0998 * wind_speed + 594455.8249

    elif 6 <= wind_speed < 7:
        wind_power_3_6 = 99800.19027 * wind_speed ** 2 + -725397.4515 * wind_speed + 1684305.255

    elif 7 <= wind_speed < 8:
        wind_power_3_6 = 101486.9799 * wind_speed ** 2 + -775460.2669 * wind_speed + 1952092.272

    elif 8 <= wind_speed <= 9:
        wind_power_3_6 = -93714.5505 * wind_speed ** 2 + 2452570.509 * wind_speed + -11379255.99

    elif 9 < wind_speed < 10:
        wind_power_3_6 = -268000 * wind_speed ** 2 + 5516000 * wind_speed + -24863000

    elif 10 <= wind_speed < 11:
        wind_power_3_6 = -52000 * wind_speed ** 2 + 1164000 * wind_speed + -2943000

    elif 11 <= wind_speed < 19.5:
        wind_power_3_6 = 3600000

    elif 19.5 <= wind_speed < 20.499:
        wind_power_3_6 = 3544000

    elif 20.499 <= wind_speed < 21.499:
        wind_power_3_6 = 3400000

    elif 21.499 <= wind_speed < 22.499:
        wind_power_3_6 = 2354000

    elif wind_speed < 23.499:
        wind_power_3_6 = 2050000

    elif wind_speed < 25.01:
        wind_power_3_6 = 1280000
    else:
        wind_power_3_6 = 0

    return wind_power_3_6


# =====================================================================


def calculate_wind_power_3_8(wind_speed):
    """Calculate wind power 3.8 based on passing parameters"""

    wind_power_3_8 = 0
    if wind_speed < 2.75:
        wind_power_3_8 = 0

    elif 2.75 <= wind_speed < 4:
        wind_power_3_8 = 38594.4795 * wind_speed ** 2 + -91774.18866 * wind_speed + -6930.505107

    elif 4 <= wind_speed < 5:
        wind_power_3_8 = 50328.66804 * wind_speed ** 2 + -179633.9254 * wind_speed + 156761.425

    elif 5 <= wind_speed < 6:
        wind_power_3_8 = 70574.72694 * wind_speed ** 2 + -368403.0998 * wind_speed + 594455.8249

    elif 6 <= wind_speed < 7:
        wind_power_3_8 = 99800.19027 * wind_speed ** 2 + -725397.4515 * wind_speed + 1684305.255

    elif 7 <= wind_speed < 8:
        wind_power_3_8 = 101486.9799 * wind_speed ** 2 + -775460.2669 * wind_speed + 1952092.272

    elif 8 <= wind_speed < 9:
        wind_power_3_8 = -71170.6037 * wind_speed ** 2 + 2080595.387 * wind_speed + -9846267.613

    elif 9 <= wind_speed < 10:
        wind_power_3_8 = -270913.0779 * wind_speed ** 2 + 5700010.426 * wind_speed + -26241862.55

    elif 10 <= wind_speed < 11:
        wind_power_3_8 = -232547.8914 * wind_speed ** 2 + 5010571.8 * wind_speed + -23283994.94

    elif 11 <= wind_speed < 12:
        wind_power_3_8 = -12000 * wind_speed ** 2 + 282000 * wind_speed + 2100000

    elif 12 <= wind_speed < 19.5:
        wind_power_3_8 = 3800000

    elif 19.5 <= wind_speed < 20.499:
        wind_power_3_8 = 3744000

    elif 20.499 <= wind_speed < 21.499:
        wind_power_3_8 = 3500000

    elif 21.499 <= wind_speed < 22.499:
        wind_power_3_8 = 2754000

    elif wind_speed < 23.499:
        wind_power_3_8 = 2250000

    elif wind_speed < 25.01:
        wind_power_3_8 = 1680000

    else:
        wind_power_3_8 = 0

    return wind_power_3_8


# =====================================================================
def calculate_wind_power(wind_speed, tuabin_type="3_6", tuabin_num=1):
    """Calculate wind power based on wind_speed, tuabin_type, tuabin_num"""

    wind_power = 0
    if tuabin_type == "3_6":
        wind_power = calculate_wind_power_3_6(wind_speed) * tuabin_num
    elif tuabin_type == "3_8":
        wind_power = calculate_wind_power_3_8(wind_speed) * tuabin_num

    return wind_power
