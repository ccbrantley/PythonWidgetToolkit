from PythonWidgetToolkit.Models.Shapes.Rectangle import Rectangle
from PythonWidgetToolkit.Models.Shapes.RoundedRectangle import RoundedRectangle
from PythonWidgetToolkit.Models.Shapes.Circle import Circle

class Controller:

    mouseX = 0
    mouseY = 0

    def __init__(_self):
        ...

    def displayFunction(_self):
        ...

    def idleFunction(_self):
        rr1 = RoundedRectangle(0, 9, 0, 9, _cornerRadius = 4, _outlineColor = (0, 0, 1, 1))
        rr1.drawFill()
        rr1.drawOutline()
