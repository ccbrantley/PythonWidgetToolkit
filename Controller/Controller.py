from PythonWidgetToolkit.Models.Shapes.Rectangle import Rectangle

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
