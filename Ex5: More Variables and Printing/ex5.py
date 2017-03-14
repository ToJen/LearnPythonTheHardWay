name = 'Nacho Creamybar'
age = 20
height_inches = 80.0 # inches
height_cm = height_inches * 2.54 # cm
weight_lbs = 100.0 # lbs
weight_kg = weight_lbs * 0.454 # kg
eyes = 'Brown'
teeth = 'Yellow' # true story
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches or %d cm tall." % (height_inches, height_cm)
print "He's %d pounds or %d kg heavy." % (weight_lbs, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "He's teeth are usually %s depending on the food" % teeth

print "If I add %d, %d and %d I get %d." % (age, height_inches, weight_lbs, age + height_inches + weight_lbs)
print "or"
print "If I add %d, %d and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg)