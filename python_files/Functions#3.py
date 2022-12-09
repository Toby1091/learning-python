# Write a function that takes a list of numbers as input, and returns a dictionary that contains the number of times each number 
# appears in the list. For example, if the input is [5, 3, 5, 2, 1], the output should be {5: 2, 3: 1, 2: 1, 1: 1}.

def frequency_of_numbers(numbers):  
    try:
        count_each_number = {}
        for num in numbers:
            if num not in count_each_number:
                count_each_number[num] = 1
            else:
                count_each_number[num] += 1
        return count_each_number
    except TypeError:
        print("Not a valid input")
        return {}
print(frequency_of_numbers([5, 3, 5, 2, 8, 's', 8, 8, 3]))




