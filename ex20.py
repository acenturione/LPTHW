# Learn python the Hard Way Exercise 20

from sys import argv

script, input_file = argv

# fucntion definition, reads and prints a file
def print_all(f):
    print f.read()

# funtion definition, goes to the beginning of the file
def rewind(f):
    f.seek(0)

# function definition, simply prints two variables, 'line_count' and current
# line of file f
def print_a_line(line_count, f):
    print line_count, f.readline()

# this opens the variable argumnet file
current_file = open(input_file)

print "First let's print the whole file:\n"

# this reads and prints the file
print_all(current_file)

print "Now let's rewind, king of like a tape."

# this goes the beginning of the file, i.e. first line
rewind(current_file)

print "Let's print three lines:"

# this says we are on the first line (1) and reads the current line,
# which is zero since we used the seek funtion to go to the beginning
current_line = 1
print_a_line(current_line, current_file)

# this iterates the to the second line, the readline function also moves
# to the next line
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# this iterates the to the second line, the readline function also moves
# to the next line
#current_line = current_line +1
current_line += 1
print_a_line(current_line, current_file)
