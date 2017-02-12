class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)

    def area(self):
        """
        Returns area of the square
        """
        return self.side**2

    def __str__(self):
        return 'Square with side ' + str(self.side)

    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)

    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)

    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


class Triangle(Shape):
    def __init__(self, base, height):
        """
        base and height of triangle
        """
        self.base = float(base)
        self.height = float(height)

    def area(self):
        """
        return area of triangle
        """
        return (self.base * self.height) / 2

    def __str__(self):
        return "Triangle with base {} and height {}" .format(str(self.base),
                                                             str(self.height))

    def __eq__(self, other):
        return type(other) == Triangle \
            and self.base == other.base \
            and self.height == other.height


class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shape_set = []

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be equal
        sh: shape to be added
        """
        if sh not in self.shape_set:
            self.shape_set.append(sh)

    def __iter__(self):
        """
        Returns an iterator that allows you to iterate over
        the set of shapes, one shape at a time
        """
        for i in self.shape_set:
            yield i

    def __str__(self):
        """
        Returns the string representation for a set, which consists
        of the string representation of each shape, categorized by type.
        """
        shapes = ""

        for i in range(len(self.shape_set)):
            shapes += str(self.shape_set[i]) + "\n"

        return shapes.strip()


def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the largest area
    shapes: ShapeSet
    """
    shapes_area = []
    result = ()

    for i in shapes:
        shapes_area.append(i.area())

    max_area = max(shapes_area)

    for i in shapes:
        if max_area == i.area():
            result += (i, )

    return result


def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file
    Creates and returns a ShapeSet with the shapes found
    filename: string
    """
    ss = ShapeSet()

    with open(filename) as shapes:
        for line in shapes:
            line_strip = line.strip().split(',')
            shape = line_strip[0]

            if shape == "circle":
                ss.addShape(Circle(line_strip[1]))

            if shape == "square":
                ss.addShape(Square(line_strip[1]))

            if shape == "triangle":
                ss.addShape(Triangle(line_strip[1], line_strip[2]))

    return ss


if __name__ == "__main__":
    ss = ShapeSet()

    t1 = Triangle(3, 6)
    t2 = Triangle(5, 2)
    c1 = Circle(4)
    c2 = Circle(8)
    s1 = Square(5)
    s2 = Square(6)

    ss.addShape(t1)
    ss.addShape(c1)
    ss.addShape(s1)
    ss.addShape(t1)
    ss.addShape(c2)

    print(ss)
