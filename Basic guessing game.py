old_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
intermediate_list = []
for x in old_list:
    if x < 5: 
        intermediate_list.append(x)
        intermediate_list.sort()
print(intermediate_list)

user_input = int(input("Please enter any number: "))
new_list = []
for x in old_list:
    if x < user_input: 
        new_list.append(x)
        new_list.sort()
print(new_list)