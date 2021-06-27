import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    ( 1, -1, -1), 
    ( 1,  1, -1), 
    (-1,  1, -1),
    (-1, -1, -1),
    
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1, -1,  1),
    (-1,  1,  1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),    
    
    (2, 1),    
    (2, 3),
    (2, 7),
    
    (6, 3),
    (6, 4),    
    (6, 7),
    
    (5, 1),
    (5, 4),
    (5, 7),
)

def Cube():
    glBegin(GL_LINES)
    for edge_tuple in edges:
        for vertex_nr in edge_tuple:
            glVertex3fv(vertices[vertex_nr])    
    glEnd()
    
def main():
    pygame.init()                                           # init the pygame
    display = (800, 600)                                    # variable holding resolution of our window
    pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)       # let pygame know what parameters our display is gonna have
    # pygame.display.set_mode(display, DOUBLEBUF|OPENGL)    # that's how it was specified in the vid
    
    
    # void gluPerspective(GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar);
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    # void glTranslatef(GLfloat x, GLfloat y, GLfloat z);
    # Specify the x, y, and z coordinates of a translation vector.
    glTranslatef(0.0, 0.0, -5.0)    # "you moving about the object so to speak" - vid
                                    # where the camera is I guess :)
    
    # void glRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z);
    # angle - Specifies the angle of rotation, in degrees,
    # x, y, z - Specify the x, y, and z coordinates of a vector, respectively.
    glRotatef(0, 0, 0, 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    # clear the previous frame
                                                            # we clear 'color buffer' and 'depth buffer'?
        Cube()
        pygame.display.flip()   # it's a way to update; we don't know why .flip() instead of .update()
        pygame.time.wait(10)
        
main()
        