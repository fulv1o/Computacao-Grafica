from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, radians

sides = 4 # Número de lados atuais do polígono regular
center = (0, 0) # Centro da circunferência
radius = 4 # Raio da circunferência


def __key__(key, x=None, y=None):
    global sides
    if ord(key) == 27: # ASCII para 'esc'
        exit()
    elif ord(key) == 43: # ASCII para '+'
        sides+=1
    elif ord(key) == 45: # ASCII para '-'
        if sides > 4:
            sides -= 1
    glutPostRedisplay()

def coordinates_generator(angle):
    global center # Apesar do centro ser na coordenada (0, 0) deixa ele aí caso queira trocar o eixo
    global radius

    x = center[0] + radius * cos(radians(angle)) # Coordenada x
    y = center[1] + radius * sin(radians(angle)) # Coordenada y
    return x, y

# callback
def redraw():
    global sides
    exterior_angle = 360/sides
    angle = 0

    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)


    glBegin(GL_LINE_LOOP)
    glColor3d(0, 0, 0)
    coordinates = list()
    for i in range(sides):
        coordinates.append(coordinates_generator(angle))
        angle += exterior_angle

    for i in coordinates:
        glVertex2d(i[0], i[1])
    glEnd()
    glFlush()



if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutCreateWindow('Poligono Regular - Fulvio')
    glutDisplayFunc(redraw)
    glutKeyboardFunc(__key__)
    glOrtho(-6, 6, -6, 6, -1, 1)
    glutMainLoop()
