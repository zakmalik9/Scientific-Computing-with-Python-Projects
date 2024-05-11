class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, new_width):
    self.width = new_width
  
  def set_height(self, new_height):
    self.height = new_height
  
  def get_area(self):
    area = self.width * self.height
    return area
  
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter
  
  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        for j in range(self.width):
          picture += "*"
        picture += "\n"
      return picture
  
  def get_amount_inside(self, other_shape):
    answer = 0
    if self.width >= other_shape.width and self.height >= other_shape.height:
      answer = self.get_area() // other_shape.get_area()
    return answer

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  
  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side
  
  def set_width(self, new_width):
    self.set_side(new_width)
  
  def set_height(self, new_height):
    self.set_side(new_height)
  
  def __str__(self):
    return f"Square(side={self.width})"
