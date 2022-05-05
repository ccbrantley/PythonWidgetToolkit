from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Rectangle:

    def drawOutline(_self):
        glColor4f(_self.color[0], _self.color[1], _self.color[2], _self.color[3])
        glBegin(GL_LINES)
        # Top horizontal line.
        glVertex2f(_self.x1, _self.y1)
        glVertex2f(_self.x2 + 1, _self.y1)
        # Bottom horizontal line.
        glVertex2f(_self.x1, _self.y2)
        glVertex2f(_self.x2 + 1, _self.y2)
        # Left vertical line.
        glVertex2f(_self.x1 + 1, _self.y1)
        glVertex2f(_self.x1 + 1, _self.y2)
        # Right vertical line.
        glVertex2f(_self.x2 + 1, _self.y1)
        glVertex2f(_self.x2 + 1, _self.y2)
        glEnd()

    def drawFill(_self):
        glColor4f(1, 0, 0, 1)
        glBegin(GL_TRIANGLES)
        # [\] Left side triangle.
        # Bottom left vertex.
        glVertex2f(_self.x1, _self.y1)
        # Top left vertex.
        glVertex2f(_self.x1, _self.y2 + 1)
        # Bottom right vertex.
        glVertex2f(_self.x2 + 1, _self.y1)
        # [\] Right side triangle.
        # Top left vertex.
        glVertex2f(_self.x1, _self.y2 + 1)
        # Bottom right vertex.
        glVertex2f(_self.x2 + 1, _self.y1)
        # Top right vertex.
        glVertex2f(_self.x2 + 1, _self.y2 + 1)
        glEnd()

    def __init__(_self, _x1, _x2, _y1, _y2, _color = (1, 0, 0, 1)):
        _self.x1 = _x1
        _self.x2 = _x2
        _self.y1 = _y1
        _self.y2 = _y2
        _self.width = abs(_self.x2 - _self.x1) + 1
        _self.height = abs(_self.y2 - _self.y1) + 1
        _self.color = _color
