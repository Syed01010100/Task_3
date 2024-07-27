#Write a python program to find the duplicate values in three user lists.


list1 = [100, 150, 258, 400, 500]
list2 = [100, 150, 258, 400, 500]
list3 = [100, 550, 258, 400, 600]


set1 = set(list1) # Convert  to sets
set2 = set(list2) # Convert to sets
set3 = set(list3) # Convert to sets

duplicates = set1.intersection(set2, set3) # using intersection

duplicate_list = list(duplicates) # convert to list

if len(duplicates) > 0:
    print("Duplicate elements:", duplicate_list)
else:
    print("No duplicates found.")