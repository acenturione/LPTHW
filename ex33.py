# Learn Python the Hard Way Exercise 33

# # Study drill 1 - 4:
# def convert_to_function(var, inc):
#     i = 0
#     numbers = []
#
#     while i < var:
#         print "At the top i is %d" % i
#         numbers.append(i)
#
#         i += inc
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d" % i
#
#     print "The numbers: "
#
#     for num in numbers:
#             print num

# Study drill 5:
def convert_to_function(var, inc):
    numbers = []

    for i in range(var):
        print "At the top i is %d" % i
        numbers.append(i)

        i += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
            print num


# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
#
# print "The numbers: "
#
# for num in numbers:
#     print num
