s=input("Enter any String: ")
str=""
for letter in s:
    if letter not in str:
        str+=letter
print("".join(sorted(str)))