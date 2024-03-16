s=input("Enter any String: ")
t=input("Enter another String: ")
if len(s)==len(t):
    if s in t*2:
        print(s +" and "+t+" are cyclic permutation of each other") 
    else:
        print(s +" and "+t+" aren't cyclic permutation of each other")  
else:
    print(s +" and "+t+" aren't cyclic permutation of each other") 