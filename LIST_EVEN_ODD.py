# FIND WHICH ONE IS EVEN AND ODD NUMBER ON GIVEN LIST
list = [10,501,22,37,100,999,87,351]
even = []
odd = []
for number in list: # iterating
    if number % 2 == 0: # TO CHECK CONDITION NUMBER % 2
        even.append(number) # append() method appends an element to the end of the list.
    else:
        odd.append(number)
print("Even Number is:", even)
print("ODD Number  is:", odd)







