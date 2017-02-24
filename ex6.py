# Learn Python the Hard Way Exercise 6

# defines x variable as string with an int inserted into the string
x = "There are %d types of people." % 10

# defines a binary variable
binary = "binary"

# defines do_not as a string vairable
do_not = "don't"

# defines y as a string with two other strings inserted as format charactors
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x
print x

# print variable y
print y

# print string with x variable inserted, which is another string
print "I said: %r." % x

# print string with y variable inserted, which is another string
print "I also said: '%s'." % y

# defines hilarious varable as boolean, False.
hilarious = False

# defines joke_evaluation varable as a string with a format character instered in the end
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the joke_evaluation varable and names the inserted character
print joke_evaluation % hilarious

# defines w variable as a string
w = "This is the left side of..."

# defines e variable as a string
e = "a string with a right side."

# prints string variable w and e joined together.
print w + e
