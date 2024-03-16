#i/p:a3b2c4
#o/p:aaabbcccc
input_string = input("Enter any string: ")
output = ""

prev_char = ''

for letter in input_string:
    if letter.isalpha():
        output += letter
        prev_char = letter
    elif letter.isdigit():
        output += prev_char * (int(letter) - 1)

print(output)