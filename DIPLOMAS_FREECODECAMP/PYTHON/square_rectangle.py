class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (self.width + self.height) * 2
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        return 'Too big for picture.' if self.width > 50 or self.height > 50 else f"{'*' * self.width}\n" * self.height
    def get_amount_inside(self, shape):
        return (self.width//shape.width)*(self.height//shape.height)
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        super().__init__(width=self.side, height=self.side)
    def set_side(self,side):
        self.side = side
        super().set_width(self.side)
        super().set_height(self.side)
    def set_width(self,width):
        self.side = width
        super().set_width(self.side)
        super().set_height(self.side)
    def set_height(self,height):
        self.side = height
        super().set_width(self.side)
        super().set_height(self.side)
    def __str__(self):
        return f'Square(side={self.side})'