# Learn Python the Hard Way Exercise 19

# this defines our function, with two arguments, and then prints the
# arguments out as a reference character.
def cheese_and_crackers(cheese_count, box_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of chackers!" % box_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# this calls our function, with two integers as variables
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# this call our function with two variables pointing to integers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this calls the funtion, with integars summed in the call
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# this calls the funtion with vairables added to integers
print "And we can combine the two, varables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
