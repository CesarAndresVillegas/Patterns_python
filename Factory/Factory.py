import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return self.side * 4


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class ShapeFactory:
    @staticmethod
    def create_shape(shape, attributes={}):
        current_shapes = {
            "Circle": Circle(attributes['radius']),
            "Square": Square(attributes['side']),
            "Rectangle": Rectangle(attributes['height'], attributes['width'])}

        return current_shapes.get(shape, 'Error -> Arise an exception')


def shape_client():
    desired_shape = 'Square'
    attributes = {"side": 2}

    shape = ShapeFactory.create_shape(desired_shape, attributes)
    print(shape.__dict__)


if __name__ == '__main__':
    shape_client()
