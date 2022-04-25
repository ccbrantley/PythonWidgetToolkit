from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy

def drawRectangle(_x, _y, _width, _height, _radius, _color = (1, 0, 0), _lineWidth = 1):
    glLineWidth(_lineWidth)
    glColor3f(_color[0], _color[1], _color[2])
    drawRect(_x, _y, _width, _height, _radius)

def drawRect(_x, _y, _width, _height, _radius):

    glBegin(GL_LINES)

    # Top side of rectangle.
    glVertex2f(_x + _radius, _y)
    glVertex2f(_x + _width - _radius, _y)

    # Right side of rectangle.
    glVertex2f(_x + _width, _y - _radius)
    glVertex2f(_x + _width, _y - _height + _radius)

    # Bottom side of rectangle.
    glVertex2f(_x + _radius, _y - _height)
    glVertex2f(_x + _width - _radius, _y - _height)

    # Left side of rectangle.
    glVertex2f(_x, _y - _radius)
    glVertex2f(_x, _y - _height + _radius)

    glEnd()

    # Top right corner.

    h = _x + _width - _radius
    k = _y - _radius
    glBegin(GL_LINE_STRIP)
    for x in range(_x + _width - _radius, _x + _width + 1):
        y = k + (_radius ** 2 - (x - h) ** 2) ** (1 / 2)
        glVertex2f(x, y)
    glEnd()

    # Bottom right corner.

    h = _x + _width - _radius
    k = _y - _height + _radius
    glBegin(GL_LINE_STRIP)
    for x in range(_x + _width - _radius, _x + _width + 1):
        y = k - (_radius ** 2 - (x - h) ** 2) ** (1 / 2)
        glVertex2f(x, y)
    glEnd()

    # Bottom left corner.

    h = _x + _radius
    k = _y - _height + _radius
    glBegin(GL_LINE_STRIP)
    for x in range(_x + _radius, _x - 1, -1):
        y = k - (_radius ** 2 - (x - h) ** 2) ** (1 / 2)
        glVertex2f(x, y)
    glEnd()

    # Top left corner.

    h = _x + _radius
    k = _y - _radius
    glBegin(GL_LINE_STRIP)
    for x in range(_x, _x + _radius + 1):
        y = k + (_radius ** 2 - (x - h) ** 2) ** (1 / 2)
        glVertex2f(x, y)
    glEnd()

def displayFunction():
    idleFunction()

def reinitProjection():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def idleFunction():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    reinitProjection()
    drawRectangle(150, 350, 200, 200, 10, _lineWidth = 3)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("")
    glutDisplayFunc(displayFunction)
    glutIdleFunc(idleFunction)
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
    glutMainLoop()
main()
