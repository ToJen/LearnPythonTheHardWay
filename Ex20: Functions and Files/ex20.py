from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Let's print the whole file:\n"
print_all(current_file)
# print current_file.read()   # also works
print "\n"

print "Now let's rewind, like a tape."
rewind(current_file)

print "Let's print three lines:"

curr_line = 1
print_a_line(curr_line, current_file)
curr_line = curr_line+1
print_a_line(curr_line, current_file)
# curr_line++ # not supported
curr_line += 1
print_a_line(curr_line, current_file)