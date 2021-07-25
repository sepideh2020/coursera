# Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals). Do not rewrite the dictionary.

swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}

swimmers['Phelps'] = swimmers['Phelps'] + 5
# ex
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():  # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

# ex
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)

# ex
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for k in inventory:
    print("Got", k, "that maps to", inventory[k])

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

print(type(inventory.keys()))

# ex
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))
# Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!
places = {"Australia": 2000, "Greece": 2004, "China": 2008, "England": 2012}

places['Brazil'] = 2016
# We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

events = list(medal_events.keys())

# If you want to modify a dictionary and keep a copy of the original, use the dictionary copy method. Since acopy is a copy of the dictionary, changes to it will not effect the original.
acopy = opposites.copy()
acopy['right'] = 'left'  # does not change opposites
