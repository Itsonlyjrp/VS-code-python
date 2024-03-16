s1=input("Enter First String:")
s2=input("Enter Second String:")
t1="".join(sorted(s1))
t2="".join(sorted(s2))
if t1==t2:
    print("Same characters in both strings")
else:
    print("Not same characters in both strings")