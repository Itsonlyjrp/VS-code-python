# s=input("Enter any String: ")
# str=""
# for letter in s:
#     if letter not in str:
#         str+=letter
# if "".join(sorted(s))=="".join(sorted(str)):
#     print("No repetition of characters in "+s)
# else:
#     print("Repetition of characters in "+s)
s=input("Enter any String: ")
str=""
for letter in s:
    if letter not in str:
        str+=letter
    else:
        print("Repetition of characters in "+s)
        break
else:
    print("No repetition of characters in "+s)