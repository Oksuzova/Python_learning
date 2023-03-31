class TriangleChecker:

    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return "Yes, this triangle exist!"
                return "Sorry, this triangle does not exist"
            return "Side should be > 0."
        return "Side should be an integer."


tringle = TriangleChecker([2, 5, 4])
print(tringle.is_triangle())
