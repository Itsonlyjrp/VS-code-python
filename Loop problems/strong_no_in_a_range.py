n=int(input("Enter any integer: "))
for given_no in range(1,n+1):
    temp=given_no
    sum=0
    while(temp!=0):
            fact=1
            last=temp%10
            for j in range(1,last+1):
             fact=fact*j
            sum=sum+fact
            temp//=10
    if(given_no==sum):
        print(given_no)
        