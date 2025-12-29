from math import pi
from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} цвета радиусом {} имеет площадь {:.2f}".format(
            self.FIGURE_TYPE, self.color.color, self.radius, self.area()
        )
