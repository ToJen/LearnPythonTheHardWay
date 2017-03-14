# run python ex16.py test.txt

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')      # w mode allows you to write to a file
# target = open(filename, 'r')    # r mode is read only; IOError: File not open for writing

print "Truncating the file..."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it"
print "Closing %r..." % filename
target.close()
print "Closed"