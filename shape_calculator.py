class Rectangle:

  def __init__(rect, width, height):
    rect.width = width
    rect.height = height

  def get_width(rect):
    return rect.width

  def get_height(rect):
    return rect.height

  def set_width(rect, width):
    rect.width = width

  def set_height(rect, height):
    rect.height = height

  def get_area(rect):
    area = rect.width * rect.height
    return area

  def get_perimeter(rect):
    perim = (2 * rect.width) + (2 * rect.height)
    return perim

  def get_diagonal(rect):
    diag = ((rect.width ** 2 + rect.height ** 2) ** .5)
    return diag

  def get_picture(rect):
    if rect.width > 50 or rect.height > 50:
      return "Too big for picture."
    else:
      wCount = 0
      wPrint = ''
      hCount = 0
      hPrint = ''
      while wCount < rect.width:
        wPrint = wPrint + '*'
        wCount += 1
      wPrint = wPrint + '\n'
      while hCount < rect.height:
        hPrint = hPrint + wPrint
        hCount += 1
      return hPrint

  def get_amount_inside(rect, other):
    other = int(rect.get_area() / other.get_area())
    return other

  def __str__(rect):
    return "Rectangle(width=" + str(rect.width) + ", height=" + str(rect.height) + ")"
    

class Square(Rectangle):

  def __init__(square, side):
    super().__init__(side, side)

  def set_side(square, side):
    square.width = side
    square.height = side

  def set_width(square, side):
    square.width = side

  def set_height(square, side):
    square.height = side

  def __str__(square):
    return "Square(side=" + str(square.width) + ")"
    