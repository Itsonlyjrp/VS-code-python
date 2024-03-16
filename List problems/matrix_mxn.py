# dimensions=input().split()
# m=int(dimensions[0])
# n=int(dimensions[1])
# l=[]
# for i in range(m):
#     new_row=[int(ele) for ele in input().split()]
#     l.append(new_row)
# print(l)

# dimensions=input().split()
# m=int(dimensions[0])
# n=int(dimensions[1])
# l=[]
# for i in range(m):
#     new_row=[]
#     for j in range(n):
#         new_row.append(int(input()))
#     l.append(new_row)
# print(l)
# dimensions=input().split()
# m=int(dimensions[0])
# n=int(dimensions[1])
# l=[]       
# elements=input().split()
# for i in range(m):
#     new_row=[]
#     for j in range(n):
#         new_row.append(int(elements[j+n*i]))
#     l.append(new_row)
# print(l)
dimensions = input().split()
m = int(dimensions[0])
n = int(dimensions[1])
l = []
elements = input().split()

for i in range(m):
    new_row = []
    for j in range(n):
        new_row.append(int(elements[j + n * i]))
    l.append(new_row)

# Print each row on a new line
for row in l:
    print(row)
    