# Learn Python the Hard Way Exercise 13

# from sys import argv
#
# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

#_______________________

# from sys import argv
#
# script, first_name = argv
# last_name = raw_input("What's your last name? ")
#
# print "Your full name is %s %s " % (first_name, last_name)

#__________________________

from sys import argv

x = argv

print "The name of this script is %s." % x[0]
feedback = raw_input("What do you think of the name, %s?" % x[0])
print "Thank you for your feedback!"
