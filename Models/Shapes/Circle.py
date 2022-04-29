from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy

class Circle:

    def __init__(_self, _h, _k, _radius):
        _self.h = _h
        _self.k = _k
        _self.radius = _radius

    def drawFill(_self, _color = (1, 0, 0, 1), _divisions = 5):

        glColor4f(_color[0], _color[1], _color[2], _color[3])

        increment = 3.14159
        glBegin(GL_TRIANGLES)
        for x in range(_divisions * (int(_self.radius / 180) + 1)):
            for inc in numpy.arange(0, 360, increment):

                # Rightmost point.
                glVertex2f(
                    _self.h + (_self.radius * math.cos(inc)),
                    _self.k + (_self.radius * math.sin(inc)),
                    )

                # Leftmost point.
                glVertex2f(
                    _self.h  + (_self.radius * math.cos(inc + increment)),
                    _self.k  + (_self.radius * math.sin(inc + increment)),
                    )

                # Center point.
                glVertex2f(
                    _self.h + (_self.radius * math.cos(inc + increment / 2)),
                    _self.k + (_self.radius * math.sin(inc + increment / 2)),
                    )
            increment /= 2
        glEnd()

    # _divisions is set to 180 to be approximate, set to 90 otherwise.
    def drawOutline(_self, _color = (1, 0, 0, 1), _lineWidth = 1, _divisions = 180):

        glColor4f(_color[0], _color[1], _color[2], _color[3])
        glLineWidth(_lineWidth)

        step = math.radians(_divisions / _self.radius)
        outlineOffset = int(_lineWidth / 2)
        glBegin(GL_LINE_STRIP)
        for radian in numpy.arange(0, 6.28319, step):
            glVertex2f(
                _self.h + ((_self.radius - outlineOffset) * math.cos(radian)),
                _self.k + ((_self.radius - outlineOffset) * math.sin(radian)),
                )
        glEnd()

    def checkIfCollision(_self, _x, _y):
        distance = ((_self.h - _x) ** 2 + (_self.k - _y) ** 2) ** (1 / 2)
        if (distance <= _self.radius):
            return True
        return False
