""" INHERITANCE """

class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    # pass    # just get what's in Parent, nothing new in Child - just an empty block
    def override(self):
        print "CHILD override"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

""" COMPOSITION """

class Other(object):

    def overide(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child_Two(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child_Two()

son.implicit()
son.override()
son.altered()