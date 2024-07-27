# Calculate first and last digit of an int.
def sum_first_last(number):
    str_num = str(number) # convert int to stg
    first_digit = int(str_num[0])
    last_digit = int(str_num[-1])
    return first_digit+last_digit
if __name__ =="__main__":
    number = 999555667799
    result = sum_first_last(number)
    print("calculate first and last digit a given input:", result)
