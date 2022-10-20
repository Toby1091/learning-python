import random
rd_num = random.randint(1,9)
print(rd_num)
user_num = 0
number_of_guesses = 0

while user_num != rd_num:
    user_num = int(input("Please try to guess the correct number between 1-9: "))
    number_of_guesses += 1
    if user_num < rd_num:
        print("too low")
    elif user_num > rd_num:
        print("too high")
    else:
        print("you won!")
        print("you took only", number_of_guesses, "tries!")
    

