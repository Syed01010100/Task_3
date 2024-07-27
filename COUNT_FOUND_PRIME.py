# Given a Python List [10,501,22,37,100,999,87,351]
# Create a new Python List which will contain all the Prime Numbers in it?
# Task is to Count all the Prime Numbers ?

# Given number list
list = [10,501,22,37,100,999,87,351]

# Empty list
prime_number = []

# Iterate through each number 
# form the list
for num in list:
    # 0 and 1 is not a prime number so skip this number
    if num == 0 or num == 1:
        continue
    # loop from 2 to half of the given number
    for i in range(2, num // 2 + 1):
        # If number is divisible by any  number (i) then it is not  a prime number
        if num % i == 0:
            break
    # If not divisible then it is a prime number
    else:
        # if number is prime then append to the list
        prime_number.append(num)

# If list is non-empty then print th elements
if len(prime_number):
    print("Prime Number is: ",prime_number)
    print("count the total number of prime number ", len(prime_number))
else:
    print("No any number from the given list is Prime")

