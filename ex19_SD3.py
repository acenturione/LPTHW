# Learn Python the Hard Way Exercise 19 SD3

def my_function(arg1, arg2):
    print "summing arg1: %r and arg2: %r..." % (arg1, arg2)
    print arg1 + arg2

print "1. Call function by inserting numbers:"
my_function(4, 44)

print "2. Call funtion by inserting strings:"
my_function('cat', 'dog')

print "3. Call funtion with integer variables"
x = 400
y = 440
my_function(x, y)

print "4. Call funtion with string variables"
a, b = 'snake', 'mouse'
my_function(a, b)

print "5. Values from other functions, here is randint:"
import random
my_function(random.randint(1,100), random.randint(1,100))

print "6. Values from raw input:"
d = raw_input("Please enter a value to be summed:")
my_function(d, d)

print "7. Values from math in function"
my_function(4 + 6, 5 + 5)

print "8. Raw input plus math"
e = raw_input("Enter a value: ")
my_function(e, e + e)

print "9. Raw input directly in the function call"
my_function(raw_input("Enter first number: "), raw_input("enter second number: "))

print "10. How about a string and an integer"
my_function(str(4), 'dogs')
