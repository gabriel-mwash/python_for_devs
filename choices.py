"""
def turn_camera_on():
    return None


if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        turn_camera_on()


if (light < 0.01) != (temperatuve > 0.0):
    turn_camera_on()

x = 5494

if x == abs(x):
    print("true")
else:
    print("false")



def different(a, b) -> bool:
    if a != b:
        return True
    else:
        return False



population = int(input("enter population: "))
land_area = int(input("enter land area: "))

if population < 10000000:
    print(population)

if 10000000 < land_area < 35000000:
    print(land_area)

if (population / land_area) > 100:
    print("densily populated")
else:
    print("sparsely populated")


ph = float(input("Enter the ph level: "))
if ph < 7.0:
    print("it's acidic!")
if ph < 4.0:
    print("It's a strong acid!")


young = age < 45
heavy = bmi >= 22.0

if young and heavy:
    risk = "medium"
elif young and not heavy:
    risk = "low"
elif not young and heavy:
    risk = "high"
elif not young and not heavy:
    risk = "medium"
"""

def convert_temperatures(t, target: str):
    """ convert temperature t from source unit to target unit
    >>> convert_temperatures(20,  fahrenheit)
    68
    >>> conert_temperatures(20, kelvin)
    293.15
    >>> convert_temperatures(20, rankine)
    527.67
    >>> convert_temperatures(20, delisle)
    120
    >>> convert_temperature(20, newton)
    6.6
    >>> convert_temperatures(20, reaumur)
    16
    >>> convert_temperatures(20, romer)
    18
    """
    if "fahrenheit" == target:
        temp_in_fah = ( 9 / 5 ) * t + 32
        print("temperature in fahrenheit is ", temp_in_fah)

    elif "kelvin" == target:
        temp_in_kev = t + 273.15
        print("temperature in kelvin is ", temp_in_kev)

    elif target == "rankine":
        temp_in_rank = (t + 273.15) * (9 / 5)
        print("temperature in rankine is ", temp_in_rank)

    elif target == "delisle":
        temp_in_del = (100 - t) * (3 / 2)
        print("temperature in delisle is ", temp_in_del)

    elif target == "newton":
        temp_in_new = t * 33 / 100
        print("temperature in newton is ", temp_in_new)

    elif target == "reaumur":
        temp_in_reau = t * 4 / 5
        print("temperature in reaumur is ", temp_in_reau)

    elif target == "romer":
        temp_in_rom = (t * 21 / 40) + 7.5
        print("temperature in romer is " , temp_in_rom)
    return


