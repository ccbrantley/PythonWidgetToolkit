from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Rectangle:
    def __init__(_self, _x, _y, _width, _height, _radius):
        _self.x = _x
        _self.y = _y
        _self.width = _width
        _self.height = _height
        _self.radius = _radius

    def draw (_self, _color = (1, 0, 0), _lineWidth = 1):

        glLineWidth(_lineWidth)
        glColor3f(_color[0], _color[1], _color[2])

        glBegin(GL_LINES)

        # Top side of rectangle.
        glVertex2f(_self.x + _self.radius, _self.y)
        glVertex2f(_self.x + _self.width - _self.radius, _self.y)

        # Right side of rectangle.
        glVertex2f(_self.x + _self.width, _self.y - _self.radius)
        glVertex2f(_self.x + _self.width, _self.y - _self.height + _self.radius)

        # Bottom side of rectangle.
        glVertex2f(_self.x + _self.radius, _self.y - _self.height)
        glVertex2f(_self.x + _self.width - _self.radius, _self.y - _self.height)

        # Left side of rectangle.
        glVertex2f(_self.x, _self.y - _self.radius)
        glVertex2f(_self.x, _self.y - _self.height + _self.radius)

        glEnd()

        # Top right corner.

        h = _self.x + _self.width - _self.radius
        k = _self.y - _self.radius
        glBegin(GL_LINE_STRIP)
        for x in range(_self.x + _self.width - _self.radius, _self.x + _self.width + 1):
            y = k + (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
        glEnd()

        # Bottom right corner.

        h = _self.x + _self.width - _self.radius
        k = _self.y - _self.height + _self.radius
        glBegin(GL_LINE_STRIP)
        for x in range(_self.x + _self.width - _self.radius, _self.x + _self.width + 1):
            y = k - (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
        glEnd()

        # Bottom left corner.

        h = _self.x + _self.radius
        k = _self.y - _self.height + _self.radius
        glBegin(GL_LINE_STRIP)
        for x in range(_self.x + _self.radius, _self.x - 1, -1):
            y = k - (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
        glEnd()

        # Top left corner.

        h = _self.x + _self.radius
        k = _self.y - _self.radius
        glBegin(GL_LINE_STRIP)
        for x in range(_self.x, _self.x + _self.radius + 1):
            y = k + (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
        glEnd()

    def checkIfCollision(_self, _x, _y):
        if ((_x >= _self.x) and (_x <= _self.x + _self.width)):
            if ((_y <= _self.y) and (_y >= _self.y - _self.height)):

                # Top to bottom rectangle collision check.
                if ((_x >= _self.x + _self.radius) and (_x <= _self.x + _self.width - _self.radius)):
                    return True

                # Left to right rectangle collision check.
                if ((_y <= _self.y - _self.radius) and (_y >= _self.y - _self.height + _self.radius)):
                    return True

                # Top right corner collision check.
                if (((_self.x + _self.width - _self.radius - _x) ** 2 + (_self.y - _self.radius - _y) ** 2) ** (1 / 2) <= _self.radius):
                    return True

                # Bottom right corner collision check.
                if (((_self.x + _self.width - _self.radius - _x) ** 2 + (_self.y - _self.height + _self.radius - _y) ** 2) ** (1 / 2) <= _self.radius):
                    return True

                # Bottom left corner collision check.
                if (((_self.x + _self.radius - _x) ** 2 + (_self.y - _self.height + _self.radius - _y) ** 2) ** (1 / 2) <= _self.radius):
                    return True

                # Top left corner collision check.
                if (((_self.x + _self.radius - _x) ** 2 + (_self.y - _self.radius - _y) ** 2) ** (1 / 2) <= _self.radius):
                    return True
        return False
