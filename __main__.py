import numpy
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PythonWidgetToolkit.Models.Shapes.Rectangle import Rectangle
from PythonWidgetToolkit.Controller.Controller import Controller

def mouseFunction(_x, _y):
    global controller
    controller.mouseX = _x
    controller.mouseY = glutGet(GLUT_WINDOW_HEIGHT) - _y - 1

def displayFunction():
    global controller
    controller.displayFunction()

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
    global controller
    controller.idleFunction()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("")
    glutDisplayFunc(displayFunction)
    glutIdleFunc(idleFunction)
    glutPassiveMotionFunc(mouseFunction)
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
    glutMainLoop()

controller = Controller()

main()
