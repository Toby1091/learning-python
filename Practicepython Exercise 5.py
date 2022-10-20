word = input("Please enter a string of letters: ")
reverse_word = word[::-1]
if word == reverse_word:
    print("this is a palindrome")
else:
    print("this is not a palindrome")