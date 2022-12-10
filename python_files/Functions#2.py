def compute_aver(numbers):
    # The following is just a shorthand for "if len(numbers)>0"
    if numbers: # Read as: if the statement "I swear, it's an empty list!" is a lie, run the code. Only if it's not a lie, run the rest
        total = sum(numbers)
        len_list = len(numbers)
        avg = total/len_list
        return avg
    else:
        return 0

print(int(compute_aver([])))

'''
Comment Chat GPT: The code above is a simpler way to check if the numbers list is empty and return 0 if it is. 
However, there are a few issues with this code that make it less clear and less efficient.
First, using the if numbers: statement to check if the list is empty is not as clear as using the if not numbers: statement. 
This is because the not operator makes it more explicit that you are checking if the numbers list is empty, and it is more common to use not in this context than to use a simple if statement without any negation.
Second, this code uses the else block to return 0 if the numbers list is empty. 
While this is a valid way to do this, it is not as efficient as simply returning 0 from the if statement itself. 
This is because the else block will be executed even if the numbers list is empty, 
which means the code inside the else block will be run unnecessarily
'''
def compute_aver(numbers):
    if not numbers: # Read as: if the statement "I swear, it's not an empty list!" is a lie, run the code. If not a lie, run the rest
        return 0
    else:
        total = sum(numbers)
        len_list = len(numbers)
        avg = total/len_list
        return avg

print(int(compute_aver([1,2,3,34,4,5])))
