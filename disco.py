from OpenGL.GL import *
from OpenGL.GLUT import *

lines = False # Variável de controle do desenvolvedor

# Cria um objeto 'trângulo' e também possui o método para desenhá-los
class Triangle:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def draw_triangle(self):
        glColor(0, 1, 1) # Ciano
        glBegin(GL_TRIANGLE_STRIP)
        glVertex2d(self.v1[0], self.v1[1])
        glVertex2d(self.v2[0], self.v2[1])
        glVertex2d(self.v3[0], self.v3[1])
        glEnd()
        glFlush()

# Desenha os contornos
def draw_lines():
    glBegin(GL_LINE_LOOP)
    glColor(0, 0, 0) # Linhas pretas

    # Quadrado Externo
    glVertex2d(2, 2)
    glVertex2d(8, 2)
    glVertex2d(8, 8)
    glVertex2d(2, 8)
    glVertex2d(2, 2)

    # Quadrado interno
    glVertex2d(4, 4)
    glVertex2d(6, 4)
    glVertex2d(6, 6)
    glVertex2d(4, 6)
    glVertex2d(4, 4)

    # Shuriken
    glVertex2d(4, 4)
    glVertex2d(2, 2)
    glVertex2d(6, 4)
    glVertex2d(8, 2)
    glVertex2d(6, 6)
    glVertex2d(8, 8)
    glVertex2d(4, 6)
    glVertex2d(2, 8)
    glVertex2d(4, 4)

    glEnd()
    glFlush()

# Não deve ser instanciada, serve para saber se o as linhas estão desenhadas ou não
def __lines__():
    global lines
    if not lines:
        draw_lines()
        lines = True
    else:
        glutPostRedisplay()
        lines = False

# Verifica qual tecla o usuário apertou
def __key__(key, x=None, y=None):
    if ord(key) == 27: # ASCII para 'esc'
        exit()
    elif ord(key) == 99: # ASCII para 'c'
        __lines__()

# Callback
def redraw():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    triangles = list()
    # Trapezio 1
    triangles.append(Triangle([2, 2], [8, 2], [6, 4]))
    triangles.append(Triangle([2, 2], [6, 4], [4, 4]))

    # Trapezio 2
    triangles.append(Triangle([8, 2], [8, 8], [6, 6]))
    triangles.append(Triangle([6, 6], [6, 4], [8, 2]))

    # Trapezio 3
    triangles.append(Triangle([6, 6], [8, 8], [4, 6]))
    triangles.append(Triangle([2, 8], [4, 6], [8, 8]))

    # Trapezio 4
    triangles.append(Triangle([2, 2], [4, 4], [2, 8]))
    triangles.append(Triangle([4, 4], [4, 6], [2, 8]))

    for i in triangles:
        i.draw_triangle()



if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutCreateWindow('Disco Quadrado - Fulvio')
    glutDisplayFunc(redraw)
    glutKeyboardFunc(__key__)
    glOrtho(0, 10, 0, 10, -1, 1)
    glutMainLoop()

