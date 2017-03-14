def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

print_two("aliko", "dangote")

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

print_two_again("tomi", "jay")

def print_one(arg1):
    print "arg1: %r" % (arg1)

print_one("@lifeoftomi")

def print_none():
    print "Nothing to print brah!"

print_none()