s=input("Enter any String: ")
for letter in s:
    if letter not in "aeiouAEIOU":
        print("Not all chars are vowel")
        break
    else:
        print("All characters are vowel")
    