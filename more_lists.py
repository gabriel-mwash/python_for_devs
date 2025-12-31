from typing import List

def remove_neg(num_list: List[float]) -> None:
    """ Remove the negative numbers from the list num_list.
    >>> remove_neg([-5, 1, -3, 2])
    [1, 2]
    """
    i = 0
    

    while i < len(num_list) - 1:
        if num_list[i] > 0:
            i = i + 1
        else:
            num_list.remove(num_list[i])
    return num_list
            

    for item in num_list:
        if item < 0:
            num_list.remove(item)

triangle_length = 7
for i in list(range(0, triangle_length)):
    print("T" * i)

for width in range(1, 8):
    print("T" * width)

for width in range(1, 8):
    print(' ' * (7 - width), "T" * width, sep="")


width = 1
while width < 8:
    print("T" * width)
    width += 1

width = 1
while width < 8:
    print(" " * (7 - width), "T" * width, sep="")
    width += 1




rat1 = [12, 9, 3, 10]
rat2 = [5, 6, 7, 8]



if rat1[0] > rat2[0] and rat1[-1] > rat2[-1]:
    print("rat one weighed more than rat 2 on day 1.")
    print("rat two became heavier thant rat 1")
else:
     print("rat 2 became heavier thatn rat 1")


if rat1[0] > rat2[0]:
    if rat1[-1] > rat2[-1]:
        print("rat 1 remained heaveri than rat2. ")
    else:
        print("rat 2 beame heavier than rat 1.")
else:
    print("rat 2 became heavier than rat 1")






rat_1_weight = 20
rat_2_weight = 30

week_count = 0
while rat_1_weight <= (1.25 * rat_1_weight) :
    rat_1_weight = 1.04 * rat_1_weight
    week_count = week_count + 1

print(week_count)
    
