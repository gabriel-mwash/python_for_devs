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
"""

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


