# Prompt user for name
name = input("What is your name?:  ")
# Print name if name is greater than 0 and consists of alphabetic characters
if len(name) > 0 and name.isalpha():
    print ("Hello " + name)
    # Print everything from the second letter onward
    first = name[0]
    new_word = name + first + "ay"
    new_word = new_word[1:len(new_word)]
    print ("Your name in pig latin is:  " + new_word)
else:
    print("Invalid input")


