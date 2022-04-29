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

    def drawFill(_self, _color = (1, 0, 0, 1)):

        glColor4f(_color[0], _color[1], _color[2], _color[3])

        glBegin(GL_TRIANGLES)

        # Middle Fill: Top left, bottom right, bottom left triangle.
        glVertex2f(_self.x + _self.radius, _self.y)
        glVertex2f(_self.x + _self.width - _self.radius, _self.y - _self.height)
        glVertex2f(_self.x + _self.radius, _self.y - _self.height)

        # Middle Fill: Top left, top right, bottom right triangle.
        glVertex2f(_self.x + _self.radius, _self.y)
        glVertex2f(_self.x + _self.width - _self.radius, _self.y)
        glVertex2f(_self.x + _self.width - _self.radius, _self.y - _self.height)

        # Left Fill: Top left, bottom right, bottom left triangle.
        glVertex2f(_self.x, _self.y - _self.radius)
        glVertex2f(_self.x + _self.radius, _self.y - _self.height + _self.radius)
        glVertex2f(_self.x, _self.y - _self.height + _self.radius)

        # Left Fill: Top left, top right, bottom right triangle.
        glVertex2f(_self.x, _self.y - _self.radius)
        glVertex2f(_self.x + _self.radius, _self.y - _self.radius)
        glVertex2f(_self.x + _self.radius, _self.y - _self.height + _self.radius)

        # Right Fill: Top left, bottom right, bottom left triangle.
        glVertex2f(_self.x + _self.width - _self.radius, _self.y - _self.radius)
        glVertex2f(_self.x + _self.width, _self.y - _self.height + _self.radius)
        glVertex2f(_self.x + _self.width - _self.radius, _self.y - _self.height + _self.radius)

        # Right Fill: Top left, top right, bottom right triangle.
        glVertex2f(_self.x + _self.width - _self.radius, _self.y - _self.radius)
        glVertex2f(_self.x + _self.width, _self.y - _self.radius)
        glVertex2f(_self.x + _self.width, _self.y - _self.height + _self.radius)

        glEnd()

        # Top right corner fill.

        h = _self.x + _self.width - _self.radius - 1
        k = _self.y - _self.radius - 1
        glBegin(GL_LINES)
        for x in range(h, _self.x + _self.width):
            y = k + (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
            glVertex2f(x, k)
        glEnd()

        # Bottom right corner fill.

        h = _self.x + _self.width - _self.radius - 1
        k = _self.y - _self.height + _self.radius + 1
        glBegin(GL_LINES)
        for x in range(h, _self.x + _self.width):
            y = k - (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
            glVertex2f(x, k)
        glEnd()

        # Bottom left corner fill.

        h = _self.x + _self.radius + 1
        k = _self.y - _self.height + _self.radius + 1
        glBegin(GL_LINES)
        for x in range(h, _self.x, -1):
            y = k - (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
            glVertex2f(x, k)
        glEnd()

        # Top left corner fill.

        h = _self.x + _self.radius + 1
        k = _self.y - _self.radius - 1
        glBegin(GL_LINES)
        for x in range(_self.x + 1, h):
            y = k + (_self.radius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x, y)
            glVertex2f(x, k)
        glEnd()

    def drawOutline (_self, _color = (1, 0, 0, 1), _lineWidth = 1):

        tempWidth = _self.width
        tempHeight = _self.height
        _self.width = int(_self.width - _lineWidth / 2) + 2 
        _self.height = int(_self.height - _lineWidth / 2)

        glLineWidth(_lineWidth)
        glColor4f(_color[0], _color[1], _color[2], _color[3])

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

        _self.width = tempWidth
        _self.height = tempHeight

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
