class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        shape = ""
        for _ in range(self.height):
            shape += "*" * self.width + "\n"
        return shape

    def get_amount_inside(self, other):
        # If the other shape is larger, it cannot fit
        if self.width < other.width or self.height < other.height:
            return 0  
        # If the other shape is the same size, it can fit once
        else:
            diagonally = self.height // other.height
            horizontally = self.width // other.width
            return diagonally * horizontally

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
        
    def __str__(self):
        return f'Square(side={self.width})'

