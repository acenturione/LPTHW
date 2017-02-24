# Learn Python the Hard Way Example 5

# my_name = 'Anthony L. Centurione'
# my_age = 31 # not a lie
# my_height = 68 # inches
# my_weight = 145 # lbs
# my_eyes = 'Green'
# my_teeth = 'White'
# my_hair = 'Brown'
#
# print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth
#
# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

name = 'Anthony L. Centurione'
age = 31 # not a lie
height = 68 # inches
heigh_cm = height * 2.54 # centimeters
weight = 145 # lbs
weight_kg = weight * .45 # kilograms
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall. That's %d centimeters." % (height, heigh_cm)
print "He's %d pounds heavy. That's %d kilograms." % (weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
