#We need to print "1/1!+2/2!+3/3!+.....+n/n!"
n=int(input("Enter any integer: "))
sum=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum=sum+(i/fact)
print(sum)