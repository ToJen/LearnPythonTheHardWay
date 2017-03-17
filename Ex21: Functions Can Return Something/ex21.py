def add(a,b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a,b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do more math with functions!"

age = add(300, 20)
height = subtract(99, 12)
weight = multiply(11, 12)
iq = divide(300, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d \n" % (age, height, weight, iq)

print "Here's a lil puzzle for you!"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That give us: ", what, "Could you do that by hand?"