from assignment9 import (Circle,
                         Square,
                         Triangle,
                         ShapeSet,
                         findLargest,
                         readShapesFromFile)


t1 = Triangle(3, 6)
t2 = Triangle(2, 6)
t3 = Triangle(5, 3)
t4 = Triangle(7, 2)
t5 = Triangle(2, 6)


def test_Triangle_area():
    assert t1.area() == 9
    assert t2.area() == 6
    assert t3.area() == 7.5
    assert t4.area() == 7


def test_Triangle_str():
    assert str(t1) == 'Triangle with base 3.0 and height 6.0'
    assert str(t3) == 'Triangle with base 5.0 and height 3.0'


def test_Triangle_eq():
    assert (t1 == t2) is False
    assert (t2 == t5) is True
    assert (t3 == t4) is False


ss1 = ShapeSet()

t11 = Triangle(3, 6)
t12 = Triangle(5, 2)
c11 = Circle(4)
c12 = Circle(8)
s11 = Square(5)
s12 = Square(6)
s13 = Square(5)

ss1.addShape(t11)
ss1.addShape(t12)
ss1.addShape(c12)
ss1.addShape(c11)
ss1.addShape(s11)
ss1.addShape(s12)
ss1.addShape(s13)

ss2 = ShapeSet()

t21 = Triangle(2.0, 7)
t22 = Triangle(2.0, 7)
c21 = Circle(4)
c22 = Circle(4)
s21 = Square(9)
s22 = Square(2)
s23 = Square(2)

ss2.addShape(t21)
ss2.addShape(t22)
ss2.addShape(c22)
ss2.addShape(c21)
ss2.addShape(s21)
ss2.addShape(s22)
ss2.addShape(s23)


def test_ShapeSet_addShape():
    assert ss1.shape_set == [t11, t12, c12, c11, s11, s12]
    assert ss2.shape_set == [t21, c22, s21, s22]


def test_ShapeSet_str():
    assert str(ss1) == "{}\n{}\n{}\n{}\n{}\n{}" .format(t11,
                                                        t12,
                                                        c12,
                                                        c11,
                                                        s11,
                                                        s12)
    assert str(ss2) == "{}\n{}\n{}\n{}" .format(t21,
                                                c22,
                                                s21,
                                                s22)


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
