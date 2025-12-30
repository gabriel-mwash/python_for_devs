def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

print(f"sword length : {sword_length} meters")
print(f"sword attack area: {area_of_circle(sword_length)} square meters")
print(f"spear_length {spear_length} meters")
print(f"spear attack area: {spear_area} square meters")


damage_one = 2
damage_two = 4
damage_three = 3
damage_four = -1
damage_five = 10
damage_six = 5


def triple_attack(slash_one, slash_two, slash_three):
    return slash_one + slash_two + slash_three


result = triple_attack(2, damage_two, 89)
print(f"Result = {result}")



print("Getting dmage for", damage_one, damage_two, "and", damage_three, "....")
print(triple_attack(damage_one, damage_two, damage_three), "points of damage dealt!")
print("=========================================")

print("Getting damage for", damage_four, damage_five, "and", damage_six, "...")
print(triple_attack(damage_four, damage_five, damage_six), "points of damage dealt!")
print("=====================================")
