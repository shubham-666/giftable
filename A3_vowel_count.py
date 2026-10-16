text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Number of vowels:", count)
