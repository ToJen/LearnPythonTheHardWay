from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)   # from_file must already exist
indata = in_file.read()

# indata = open(from_file).read() # shorter way to write lines 8 and 9

print "The input file is %s bytes long." % len(indata)

print "Does the output fileexist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright all done."

out_file.close()
in_file.close()