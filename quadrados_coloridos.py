from OpenGL.GL import *
from OpenGL.GLUT import *

# Cria um objeto 'quadrado' e também possui o método para desenhá-lo
class Square:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos

    def draw_square(self):
        glColor3d(self.color[0], self.color[1], self.color[2])
        glBegin(GL_POLYGON)
        glVertex2d(self.pos[0][0], self.pos[0][1])
        glVertex2d(self.pos[1][0], self.pos[1][1])
        glVertex2d(self.pos[2][0], self.pos[2][1])
        glVertex2d(self.pos[3][0], self.pos[3][1])
        glEnd()
        glFlush()

# Verifica qual tecla o usuário apertou
def __key__(key, x=None, y=None):
    if ord(key) == 27: # ASCII para 'esc'
        exit()

# callback
def redraw():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    squares = list()
    # Criando as instâncias de quadrados
    # Coluna 1
    squares.append(Square([0, 0, 0],       [[1,  1], [5,  1], [5, 5],  [1,  5]])) # preto
    squares.append(Square([1, 0, 0],       [[1, 6],  [5, 6],  [5, 10], [1, 10]]))# vermelho
    squares.append(Square([0, 1, 0],       [[1, 11], [5, 11], [5, 15], [1, 15]])) # verde

    # Coluna 2
    squares.append(Square([0, 0, 1],       [[6, 1],  [10, 1],  [10, 5],   [6, 5]])) # azul
    squares.append(Square([1, 0, 1],       [[6, 6],  [10, 6],  [10, 10],  [6, 10]])) # lilás
    squares.append(Square([0, 1, 1],       [[6, 11], [10, 11], [10, 15],  [6, 15]])) # ciano

    # Coluna 3
    squares.append(Square([1, 1, 0],       [[11, 1],  [15, 1],  [15, 5],  [11, 5]]))  # amarelo
    squares.append(Square([0.5, 0, 0],     [[11, 6],  [15, 6],  [15, 10], [11, 10]])) # vinho
    squares.append(Square([0.5, 0.5, 0.5], [[11, 11], [15, 11], [15, 15], [11, 15]]))  # cinza

    for i in squares:
        i.draw_square()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutCreateWindow('Quadrados Coloridos - Fulvio')
    glutDisplayFunc(redraw)
    glutKeyboardFunc(__key__)
    glOrtho(0, 16, 0, 16, -1, 1)
    glutMainLoop()