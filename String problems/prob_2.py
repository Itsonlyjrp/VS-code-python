#i/p:aaabbcccc
#o/p:a3b2c4
input_string = input("Enter any string: ")
output = ""

prev_char =input_string[0]

count=1

for char in input_string[1:]:
    if char==prev_char:
       count+=1 
    else:
        output+=prev_char+str(count)
        prev_char = char 
        count=1
output+=prev_char+str(count)

print(output)

        
        