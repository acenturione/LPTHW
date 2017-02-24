# Edited in Vim

cars = 100  # This vairable is the total number of cars.
space_in_a_car = 4.0  # This variable is the number of seats in a car. Float
drivers = 30  # This is the number of human drivers.
passengers = 90  # This is the number of drivers.
cars_not_driven = cars - drivers  # This is the number of parked cars, not driven.
cars_driven = drivers  # The number of cars driven is equal to the avialable drivers.
carpool_capacity = cars_driven * space_in_a_car  # Avialable seats.
average_passengers_per_car = passengers / cars_driven  # The number of passengers diveded by the avialable seats.

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
