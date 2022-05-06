from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class RoundedRectangle:

    def drawOutline(_self):
        glColor4f(_self.outlineColor[0], _self.outlineColor[1], _self.outlineColor[2], _self.outlineColor[3])
        glBegin(GL_LINES)
        # Top horizontal line.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y2)
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y2)
        # Bottom Horizontal line.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y1)
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y1)
        # Left vertical line.
        glVertex2f(_self.x1 + 1, _self.y1 + _self.cornerRadius)
        glVertex2f(_self.x1 + 1, _self.y2 + 1 - _self.cornerRadius)
        # Right vertical line.
        glVertex2f(_self.x2 + 1, _self.y1 + _self.cornerRadius)
        glVertex2f(_self.x2 + 1, _self.y2 + 1 - _self.cornerRadius)
        glEnd()
        # Top left corner.
        topLeftY = []
        h = _self.x1 + _self.cornerRadius
        k = _self.y2 - _self.cornerRadius
        glBegin(GL_LINE_STRIP)
        for x in range(_self.x1, _self.x1 + _self.cornerRadius):
            y = k + (_self.cornerRadius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x + 1, y)
            topLeftY.insert(0, y)
        glEnd()
        # Top right corner.
        glBegin(GL_LINE_STRIP)
        for x, y in zip(
            range(_self.x2 - _self.cornerRadius, _self.x2),
            topLeftY,
        ):
            glVertex2f(x + 1, y)
        glEnd()
        # Bottom left corner.
        bottomLeftY = []
        h = _self.x1 + _self.cornerRadius
        k = _self.y1 + _self.cornerRadius
        glBegin(GL_LINE_STRIP)
        for x in range(_self.x1, _self.x1 + _self.cornerRadius):
            y = k - (_self.cornerRadius ** 2 - (x - h) ** 2) ** (1 / 2)
            glVertex2f(x + 1, y + 1)
            bottomLeftY.insert(0, y)
        glEnd()
        # Bottom right corner.
        glBegin(GL_LINE_STRIP)
        for x, y in zip(
            range(_self.x2 - _self.cornerRadius, _self.x2),
            bottomLeftY,
        ):
            glVertex2f(x + 1, y + 1)
        glEnd()

    def drawFill(_self):
        glColor4f(_self.fillColor[0], _self.fillColor[1], _self.fillColor[2], _self.fillColor[3])
        # (\][ \ ][\) Left face.
        glBegin(GL_TRIANGLES)
        # Left triangle.
        # Bottom left vertex.
        glVertex2f(_self.x1, _self.y1 + _self.cornerRadius)
        # Top left vertex.
        glVertex2f(_self.x1, _self.y2 - _self.cornerRadius + 1)
        # Bottom right vertex.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y1 + _self.cornerRadius)
        # Right triangle.
        # Top right vertex.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y2 - _self.cornerRadius + 1)
        # Top left vertex.
        glVertex2f(_self.x1, _self.y2 - _self.cornerRadius + 1)
        # Bottom right vertex.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y1 + _self.cornerRadius)
        # (\][ \ ][\) Right face.
        # Left triangle.
        # Bottom left vertex.
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y1 + _self.cornerRadius)
        # Top left vertex.
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y2 - _self.cornerRadius + 1)
        # Bottom right vertex.
        glVertex2f(_self.x2 + 1, _self.y1 + _self.cornerRadius)
        # Right triangle.
        # Top right vertex.
        glVertex2f(_self.x2 + 1, _self.y2 - _self.cornerRadius + 1)
        # Top left vertex.
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y2 - _self.cornerRadius + 1)
        # Bottom right vertex.
        glVertex2f(_self.x2 + 1, _self.y1 + _self.cornerRadius)
        # (\][ \ ][\) Middle face.
        # Left triangle.
        # Bottom left vertex.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y1)
        # Top left vertex.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y2 + 1)
        # Bottom right vertex.
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y1)
        # Right triangle.
        # Top right vertex.
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y2 + 1)
        # Top left vertex.
        glVertex2f(_self.x1 + _self.cornerRadius, _self.y2 + 1)
        # Bottom right vertex.
        glVertex2f(_self.x2 - _self.cornerRadius + 1, _self.y1)
        glEnd()
        # Top left and right corners.
        h = _self.x1 + _self.cornerRadius
        k = _self.y2 - _self.cornerRadius
        glBegin(GL_LINES)
        for x1, x2 in zip(
            range(_self.x1 + 1, _self.x1 + _self.cornerRadius),
            range(_self.x2 - 1, _self.x2 - _self.cornerRadius, -1),
        ):
            y1 = k + (_self.cornerRadius ** 2 - (x1 - h) ** 2) ** (1 / 2)
            # Left corner.
            glVertex2f(x1 + 1, y1)
            glVertex2f(x1 + 1, k)
            # Right corner.
            glVertex2f(x2 + 1, y1)
            glVertex2f(x2 + 1, k)
        # Bottom left and right corners.
        h = _self.x1 + _self.cornerRadius
        k = _self.y1 + _self.cornerRadius
        for x1, x2 in zip(
            range(_self.x1 + 1, _self.x1 + _self.cornerRadius),
            range(_self.x2 - 1, _self.x2 - _self.cornerRadius, -1),
        ):
            y1 = k - (_self.cornerRadius ** 2 - (x1 - h) ** 2) ** (1 / 2)
            # Left corner.
            glVertex2f(x1 + 1, k)
            glVertex2f(x1 + 1, y1 + 1)
            # Right corner.
            glVertex2f(x2 + 1, k)
            glVertex2f(x2 + 1, y1 + 1)
        glEnd()

    def __init__(_self, _x1, _x2, _y1, _y2, _fillColor = (1, 0, 0, 1), _outlineColor = (0, 0, 1, 1), _cornerRadius = 0):
        _self.x1 = _x1
        _self.x2 = _x2
        _self.y1 = _y1
        _self.y2 = _y2
        _self.width = abs(_self.x2 - _self.x1) + 1
        _self.height = abs(_self.y2 - _self.y1) + 1
        _self.fillColor = _fillColor
        _self.outlineColor = _outlineColor
        _self.cornerRadius = _cornerRadius
