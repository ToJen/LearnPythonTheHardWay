def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man, that's enough for a party!\nGet a blanket.\n"

print "The function numbers can be passed directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script"
num_cheese = 99
num_crackers = 101
cheese_and_crackers(num_cheese, num_crackers)

print "We can even do some math in it!"
cheese_and_crackers(10*3, 100/2)

print "Guess what? We can combine both:"
cheese_and_crackers(num_cheese+120, num_crackers+200)