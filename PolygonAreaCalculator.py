class Rectangle:
    def __init__(self, width : int, height : int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width : int) -> None:
        self.width = width
    
    def set_height(self, height : int) -> None:
        self.height = height
    
    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, shape) -> int:
        if isinstance(shape, Rectangle) or isinstance(shape, Square):
             return (self.width // shape.width) * (self.height // shape.height)
        return 0

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"{self.__class__.__name__}(side={self.width})"

print('Task 6 Testing:')
print(Rectangle(3, 6))

print('Task 7 Testing:')
print(Square(5))

print('Task 8 Testing:')
print(Rectangle(3, 6).get_area())

print('Task 9 Testing:')
print(Square(5).get_area())

print('Task 10 Testing:')
print(Rectangle(3, 6).get_perimeter())

print('Task 11 Testing:')
print(Square(5).get_perimeter())

print('Task 12 Testing:')
print(Rectangle(3, 6).get_diagonal())

print('Task 20 Testing:')
print(Rectangle(15,10).get_amount_inside(Square(5)))

print('Task 21 Testing:')
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))

print('Task 22 Testing:')
print(Square(10).get_amount_inside(Rectangle(3, 6)))