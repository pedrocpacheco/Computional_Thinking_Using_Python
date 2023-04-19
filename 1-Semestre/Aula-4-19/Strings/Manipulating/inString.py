# Seeing if a term exists in a String
message = "This is a message!"
term= input("Type the term you want to know if is in the list: \n")

if term in message:
    print("The term:", term, "exists in message!")
else:
    print("The term:", term, "doesn't exists in message!")