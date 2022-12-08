def compute_aver(numbers):
    if numbers: # Read as: if the statement "I swear, it's an empty list!" is a lie, run the code. Only if it's not a lie, run the rest
        total = sum(numbers)
        len_list = len(numbers)
        avg = total/len_list
        return avg
    else:
        return 0

print(int(compute_aver([1,2,3,34,4,5])))


def compute_aver(numbers):
    if not numbers: # Read as: if the statement "I swear, it's not an empty list!" is a lie, run the code. If not a lie, run the rest
        return 0
    else:
        total = sum(numbers)
        len_list = len(numbers)
        avg = total/len_list
        return avg

print(int(compute_aver([1,2,3,34,4,5])))
