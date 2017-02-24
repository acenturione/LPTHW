# Learn Python the Hard Way Exercise 15

# # import argv from sys so we can call argument variables in script
# from sys import argv
#
# # defining the argument variables
# script, filename = argv
#
# # defines a variable txt that is the file we are opening
# txt = open(filename)
#
# # prints a line of text naming the file
# print "Here's your file %r:" % filename
# # takes the txt variable (which is the openned file), reads the file and prints it.
# print txt.read()

# this is just a simple string print
print "Type the filename again:"
# this defines a variable file_again that is the file name
# recieved from the user via raw_input
file_again = raw_input("> ")

# this takes the file name variable and opens it and defines it as another variable
text_again = open(file_again)

# this reads the openned file and prints it.
print text_again.read()

# This closes the file to reserve system memory
text_again.close()
