#Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.
practice=('y', 'h','z','x')
#Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.
tup1="a","b","c"
# Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'),
            ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'),
            ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'),
            ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = []
for tup in lst_tups:
    t_check.append(tup[2])

# Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds=[]
for tup in tups:
    seconds.append(tup[1])
#ex
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

#ex
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)
#Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. It should return a tuple of these variables in this order.
def information(name, birth_year, fav_color,hometown):
    return(name, birth_year, fav_color,hometown)

