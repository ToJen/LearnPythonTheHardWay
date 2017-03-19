"""
stuff = {'name': 'Tomi', 'age': 19, "height": 6 * 12 + 2}
print stuff

print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = "Lagos"
print stuff['city']
print stuff

stuff[1] = "bruh!"
stuff[2] = "duuuude"

print stuff[1]
print stuff[2]
print stuff

del stuff['city']
del stuff[1]
del stuff[2]
print stuff
"""

# creates mapping of a state to an abbreviation
states = {
    'Lagos': 'LA',
    'Rivers': 'RI',
    'Sokoto': 'SO',
    'Zamfara': 'ZA',
    'Cross River': 'CR'
}

# creates some states and cities in them
cities = {
    'RI': 'Port Harcourt',
    'ZA': 'Gusau',
    'CR': 'Calabar'
}

# add more cities
cities['LA'] = 'Ikeja'
cities['SO'] = 'Wamako'

# print out some cities
print '-' * 10
print "LA state has: ", cities['LA']
print "SO state has: ", cities['SO']

# print some states
print '-' * 10
print "Rivers' abbreviation is: ", states['Rivers']
print "Zamfara' abbreviation is: ", states['Zamfara']

# print cities in the state
print '-' * 10
print "Rivers has: ", cities[states['Rivers']]
print "Zamfara has: ", cities[states['Zamfara']]

# print all cities in state
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated as %s and has city %s" % (
        state, abbrev, cities[abbrev] )

print '-' * 10
# safely get an abbreviation of a state that might not have been created
state = states.get("Federal Capital Territory")

if not state:
    print "Sorry, state not found"

# get a city with a default value
city = cities.get('FC', "Does Not Exist")
print "The city for the state 'FC' is: %s" % city