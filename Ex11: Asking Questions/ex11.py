print "How old are you?",   # comma at the end prevents from going to a new line like Java's print() vs println()
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r years old, %r feet tall and weigh %r lbs." \
    %  (age, height, weight)    # backslash continues a line into next
