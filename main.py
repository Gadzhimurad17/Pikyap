from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import matplotlib.pyplot as plt

def main():
    N = 5

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(rectangle)
    print(circle)
    print(square)

    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Пример графика")
    plt.show()

if __name__ == "__main__":
    main()
