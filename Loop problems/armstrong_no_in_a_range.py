n=int(input("Enter any integer: "))
for i in range(1,n+1):
    temp=given_no=i
    c=0
    sum=0
    while temp!=0:
        c+=1
        temp=temp//10
    while i!=0:
        last=i%10
        sum=sum+last**c
        i=i//10
    if(sum==given_no):
        print(sum)