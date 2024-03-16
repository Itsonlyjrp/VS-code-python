n=int(input("Enter any integer: "))
given_no=n
sum=0
while(n!=0):
        fact=1
        last=n%10
        for j in range(1,last+1):
         fact=fact*j
        sum=sum+fact
        n=n//10
if(given_no==sum):
    print("Strong no.")
else:
    print("Not a strong no.")