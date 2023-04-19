# Creating a String
text="0123456789"

# Printing the especific character
character = input("Type the character in the text you want to print: \n")
print(text[int(character)])

# Printing a part of the text
print(text[0:5])
print(text[5:11])

# Printing with a especif interval
print(text[0:10:3]) # 0 -> 3 -> 6 -> 9
print(text[0:10:2]) # 0 -> 2 -> 4 -> 6 -> 8