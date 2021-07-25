# Return Value Tests
def square(x):
    return x * x


assert square(3) == 9
assert square(2) == 4
assert square(0) == 0
assert square(-2) == 4


# side Effect Tests
def update_counts(letters, counts_d):
    for c in letters:

        if c in counts_d:
            counts_d[c] = counts_d[c] + 1

        else:
            counts_d[c] = 1


counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3

################################
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7

