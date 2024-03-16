n=int(input("Enter any integer: "))
print("Factors of",n,"are: ",end='\n')
for i in range(1,n+1):
  if(n%i==0):
      print(i)