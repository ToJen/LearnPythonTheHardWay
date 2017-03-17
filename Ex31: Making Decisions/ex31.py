print "You go through a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "[1] Take the cake!\n[2] Scream at the bear!!\n[3] Seize the means of cake production!!!"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. God job!?"
    elif bear == "2":
        print "The bear eats your legs off."
    else:
        print "Well, maybe doing %s is better. Bear runs away"

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina"
    print "[1] Bluberries\n[2] Yellow jacket\n[3] This makes no sense"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello."
    else:
        print "This is just some weird code"

else:
    print "You become Chuck Norris"