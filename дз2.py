#Завдання 4
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


# Приклад використання
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"Ширина: {rect.width}, Висота: {rect.height}")
    print("Площа:", rect.calculate_area())         # 15
    print("Периметр:", rect.calculate_perimeter())  # 16
