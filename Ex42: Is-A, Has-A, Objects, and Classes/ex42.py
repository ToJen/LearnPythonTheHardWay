## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        self.name = name


## Person is-a object
class Person(object):

    def __init__(self, name):
        self.name = name
        ## Person has-a pet
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name) ## use parent function to set name
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

stan = Cat("Stan")

sally = Person("Sally")

sally.pet = rover

frank = Employee("Frank", 10000)

frank.pet = stan ## remember that Employee is-a Person and inherits all its functions and  variables

flipper = Fish()

crouse = Salmon()

harry = Halibut()