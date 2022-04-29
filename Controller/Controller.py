from PythonWidgetToolkit.Models.Shapes.Rectangle import Rectangle
from PythonWidgetToolkit.Models.Shapes.Circle import Circle

class Controller:

    mouseX = 0
    mouseY = 0

    def __init__(_self):
        ...

    def displayFunction(_self):
        ...

    def idleFunction(_self):
        r1 = Rectangle(150, 350, 200, 200, 10)
        r1.drawFill()
        r1.drawOutline(_color = (0, 0, 1, 1), _lineWidth = 5)
        print(r1.checkIfCollision(_self.mouseX, _self.mouseY))
        c1 = Circle(250, 250, 100)
        c1.drawFill(_color = (0, 1, 0, 1))
        c1.drawOutline(_color = (0, 0, 1, 1), _lineWidth = 5)
