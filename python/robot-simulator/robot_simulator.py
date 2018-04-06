from operator import add
import re

# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        if self.bearing == 0:
            self.coordinates = tuple(map(add, self.coordinates, (0, 1)))
        if self.bearing == 1:
            self.coordinates = tuple(map(add, self.coordinates, (1, 0)))
        if self.bearing == 2:
            self.coordinates = tuple(map(add, self.coordinates, (0, -1)))
        if self.bearing == 3:
            self.coordinates = tuple(map(add, self.coordinates, (-1, 0)))

    def simulate(self, instructions: str) -> ():
        if not re.match(r'', instructions):
            raise ValueError("Improper instructions received. Valid values are L, R, and A.")
        for char in instructions:
            if char.upper() == "R":
                self.turn_right()
            if char.upper() == "L":
                self.turn_left()
            if char.upper() == "A":
                self.advance()
