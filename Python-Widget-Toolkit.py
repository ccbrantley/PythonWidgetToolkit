from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy
from Rectangle import Rectangle

def drawRectangle(_x, _y, _width, _height, _radius, _color = (1, 0, 0), _lineWidth = 1):
    glLineWidth(_lineWidth)
    glColor3f(_color[0], _color[1], _color[2])
    drawRect(_x, _y, _width, _height, _radius)

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
    r1 = Rectangle(150, 350, 200, 200, 10)
    r1.draw()
    #drawRectangle(150, 350, 200, 200, 10, _lineWidth = 3)
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
