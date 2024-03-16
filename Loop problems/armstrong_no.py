n=int(input("Enter any integer: "))
temp=given_no=n
c=0
sum=0
while temp!=0:
    c+=1
    temp=temp//10
while n!=0:
    last=n%10
    sum=sum+last**c
    n=n//10
if (sum==given_no):
    print("Armstrong no")
else:
    print("Not an Armstrong no")