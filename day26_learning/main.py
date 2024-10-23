import random
names = ["alex","beth","caroline","dave","elanor","freddie"] 

students_scores = {name : random.randint(1,100) for name in names}
# print(students_scores)

# passed_students ={new_key : new_value for (key,value) in dict.items() if test}
passed_students ={name : score for (name,score) in students_scores.items() if score >=60}
print(passed_students)


# -------------------------challenge-------------
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
# # print(file1_data)
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
    
# # converted the numbers into int value
# file_1_numbers = [int(num.strip()) for num in file1_data]
# file_2_numbers = [int(num.strip()) for num in file2_data]

# # print(file_1_numbers)
# # print(file_2_numbers)

# # collecting common numbers from both the list
# result = [num for num in file_1_numbers if num in file_2_numbers]

# print(result)




# ----------------challenge---------------------
# names = ["alex","beth","caroline","dave","elanor","freddie"]

# # all names which are made of 5 or more turn them to upper case 
# new_list = [name.upper() for name in names if len(name) > 4]

# print(new_list)



# This code snippet creates a list called `numbers` containing the numbers 1 to 7. It then uses a
# list comprehension to create a new list called `new_numbers` where each element is one more than
# the corresponding element in the `numbers` list. Finally, it prints out the `new_numbers` list.
# So, the output will be `[2, 3, 4, 5, 6, 7, 8]`.




# numbers = [1,2,3,4,5,6,7]

# new_numbers = [n+1 for n in numbers]
# print(new_numbers)


# ------------------------secret formula
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
# double_list = [new_item for item in list if item in list]