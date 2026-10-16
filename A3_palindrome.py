text = input("Enter a word or string: ")
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
