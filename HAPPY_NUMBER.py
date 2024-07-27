# 3. Findout happy number given list.
List = [10, 501, 22, 37, 100, 999, 87, 351]
List1 = []
def is_happy(List):
    for i in range (len(List)):
        my_sum = List[i]
        while my_sum!=1 and my_sum !=4:
            tempsum = 0
            for digit in str(my_sum):
                tempsum += int(digit) ** 2
            my_sum = tempsum
        if my_sum == 1:
            List1.append(List[i])
    return List1
print(is_happy(List))
