n=int(input('Enter any integer: '))
sum=0
for i in range(1,n+1):
    if n%i == 0:
        sum=sum+i
if(n==sum-n):
    print("Perfect number")
else:
    print("Not a perfect number")