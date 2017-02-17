from assignment9 import (Circle,
                         Square,
                         Triangle,
                         ShapeSet,
                         findLargest)


class TestTriangle():
    def setup(self):
        self.t1 = Triangle(3, 6)
        self.t2 = Triangle(2, 6)
        self.t3 = Triangle(5, 3)
        self.t4 = Triangle(7, 2)
        self.t5 = Triangle(2, 6)

    def test_area(self):
        assert self.t1.area() == 9
        assert self.t2.area() == 6
        assert self.t3.area() == 7.5
        assert self.t4.area() == 7

    def test_str(self):
        assert str(self.t1) == 'Triangle with base 3.0 and height 6.0'
        assert str(self.t3) == 'Triangle with base 5.0 and height 3.0'

    def test_eq(self):
        assert (self.t1 == self.t2) is False
        assert (self.t2 == self.t5) is True
        assert (self.t3 == self.t4) is False


class TestShapeSet():
    def setup(self):
        self.ss1 = ShapeSet()
        self.t11 = Triangle(3, 6)
        self.t12 = Triangle(5, 2)
        self.c11 = Circle(4)
        self.c12 = Circle(8)
        self.s11 = Square(5)
        self.s12 = Square(6)
        self.s13 = Square(5)
        self.ss1.addShape(self.t11)
        self.ss1.addShape(self.t12)
        self.ss1.addShape(self.c12)
        self.ss1.addShape(self.c11)
        self.ss1.addShape(self.s11)
        self.ss1.addShape(self.s12)
        self.ss1.addShape(self.s13)
        self.l1 = [self.t11, self.t12, self.c12, self.c11, self.s11, self.s12]

        self.ss2 = ShapeSet()
        self.t21 = Triangle(2.0, 7)
        self.t22 = Triangle(2.0, 7)
        self.t23 = Triangle(4, 2)
        self.c21 = Circle(4)
        self.c22 = Circle(4)
        self.s21 = Square(9)
        self.s22 = Square(2)
        self.s23 = Square(2)
        self.s24 = Square(6)
        self.ss2.addShape(self.t21)
        self.ss2.addShape(self.t22)
        self.ss2.addShape(self.c22)
        self.ss2.addShape(self.c21)
        self.ss2.addShape(self.s21)
        self.ss2.addShape(self.s22)
        self.ss2.addShape(self.s23)
        self.l2 = [self.t21, self.c22, self.s21, self.s22]

    def test_addShape(self):
        assert (self.t11 in self.ss1) is True
        assert (self.s22 in self.ss2) is True

    def test_iter(self):
        assert all(x in self.ss1 for x in self.l1) is True

        for (index, value) in enumerate(self.ss2):
            assert (value == self.l2[index]) is True

    def test_str(self):
        assert str(self.ss1) == "{}\n{}\n{}\n{}\n{}\n{}" \
            .format(self.t11, self.t12, self.c12, self.c11, self.s11, self.s12)
        assert str(self.ss2) == "{}\n{}\n{}\n{}" \
            .format(self.t21, self.c22, self.s21, self.s22)


def test_findLargest():
    t1 = Triangle(1.2, 2.5)
    t2 = Triangle(1.6, 6.4)
    c1 = Circle(4)
    c2 = Circle(2.2)
    s1 = Square(3.6)

    ss1 = ShapeSet()

    ss1.addShape(t1)
    ss1.addShape(c1)
    ss1.addShape(s1)
    ss1.addShape(t2)
    ss1.addShape(c2)

    t3 = Triangle(3, 8)
    c3 = Circle(1)
    t4 = Triangle(4, 6)

    ss2 = ShapeSet()

    ss2.addShape(t3)
    ss2.addShape(c3)
    ss2.addShape(t4)

    assert findLargest(ss1) == (c1, )
    assert findLargest(ss2) == (t3, t4)
