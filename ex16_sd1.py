# Learn Python the Hard Way Exercise 16

from sys import argv

script, filename = argv

file_open = open(filename)
print file_open.read()
file_open.close()
