class Vector:  # Class
    """Here will be documentation of Vector class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # if you want plus two variables
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # if you want first variable minus second variable
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # Scalar multiplication
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        # Scalar division
        if scalar != 0:  # Avoid division by zero
            return Vector(self.x / scalar, self.y / scalar)
        else:
            raise ValueError("Division by zero is undefined")

    def __len__(self):  # Define len() - length
        return 2

    def __repr__(self):  # Class printing in print()
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):  # Calling object, without print()
        print(f"Someone searched me? {self.x} and {self.y} is here!")

    def __del__(self):
        print(f"Vectors {self.x} {self.y} is being destroyed.")


v1 = Vector(10, 20)
v2 = Vector(10, 20)
v3 = v1 + v2
v3()
print(v1.__doc__)  # Reading documentation
del v3  # Deleting variable
