the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# the first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "Fruits can be %s" % fruit

# we can also go through a mixed list
# we use %r here since we don't know the type of elements in the list
for i in change:
    print "I got %r" % i

# we can build lists from scratch
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list" % i
    # append is a list function
    elements.append(i)

# finally, print them out
for i in elements:
    print "Element was: %d" % i