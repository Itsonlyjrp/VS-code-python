n=int(input("Enter any integer: "))
c=0
while(n!=0):
    c+=1
    n=n//10
print("No. of digits in the given integer is:",c)