# Prompt user for name
name = raw_input("What is your name? :  ")
# Print name if name is greater than 0 and consists of alphabetic characters
if len(name) > 0 and name.isalpha():
    print name
else:
    print "invalid"


