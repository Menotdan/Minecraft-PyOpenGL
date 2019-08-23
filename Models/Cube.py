# For rendering 3D
from OpenGL.GL import *
from OpenGL.GLU import *

# Cube class
class Cube:
    def __init__(self, x, y, z, size):
        self.x = x # X position
        self.y = y # Y position
        self.z = z # Z position
        self.size = size # Cube size

        # Set vertices
        self.calcVertices()

    # Move cube
    def move(self, x, y, z):
        self.x += x # Update
        self.y += y # Update
        self.z += z # Update

        # Set vertices
        self.calcVertices()

    def changeSize(self, sizeChange):
        self.size += sizeChange # Change size

        # Set vertices
        self.calcVertices()

    # Draw cube
    def draw(self):
        #glBegin(GL_QUADS)
        #for surface in self.surfaces:

        #glEnd()

        # glBegin(GL_LINES)
        # for edge in self.edges:
        #     for vertex in edge:
        #         glVertex3fv(self.vertices[vertex])
        # glEnd()
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(-(self.size-self.x), -(self.size-self.y), (self.size+self.z))
        glTexCoord2f(1.0, 0.0); glVertex3f( (self.size+self.x), -(self.size-self.y), (self.size+self.z))
        glTexCoord2f(1.0, 1.0); glVertex3f( (self.size+self.x), (self.size+self.y), (self.size+self.z))
        glTexCoord2f(0.0, 1.0); glVertex3f(-(self.size-self.x), (self.size+self.y), (self.size+self.z))
        glTexCoord2f(1.0, 0.0); glVertex3f(-(self.size-self.x), -(self.size-self.y), -(self.size-self.z))
        glTexCoord2f(1.0, 1.0); glVertex3f(-(self.size-self.x), (self.size+self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 1.0); glVertex3f((self.size+self.x), (self.size+self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 0.0); glVertex3f((self.size+self.x), -(self.size-self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 1.0); glVertex3f(-(self.size-self.x), (self.size+self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 0.0); glVertex3f(-(self.size-self.x), (self.size+self.y), (self.size+self.z))
        glTexCoord2f(1.0, 0.0); glVertex3f((self.size+self.x), (self.size+self.y), (self.size+self.z))
        glTexCoord2f(1.0, 1.0); glVertex3f((self.size+self.x), (self.size+self.y), -(self.size-self.z))
        glTexCoord2f(1.0, 1.0); glVertex3f(-(self.size-self.x), -(self.size-self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 1.0); glVertex3f((self.size+self.x), -(self.size-self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 0.0); glVertex3f((self.size+self.x), -(self.size-self.y), (self.size+self.z))
        glTexCoord2f(1.0, 0.0); glVertex3f(-(self.size-self.x), -(self.size-self.y), (self.size+self.z))
        glTexCoord2f(1.0, 0.0); glVertex3f((self.size+self.x), -(self.size-self.y), -(self.size-self.z))
        glTexCoord2f(1.0, 1.0); glVertex3f((self.size+self.x), (self.size+self.y), -(self.size-self.z))
        glTexCoord2f(0.0, 1.0); glVertex3f((self.size+self.x), (self.size+self.y), (self.size+self.z))
        glTexCoord2f(0.0, 0.0); glVertex3f((self.size+self.x), -(self.size-self.y), (self.size+self.z))
        glTexCoord2f(0.0, 0.0); glVertex3f(-(self.size-self.x), -(self.size-self.y), -(self.size-self.z))
        glTexCoord2f(1.0, 0.0); glVertex3f(-(self.size-self.x), -(self.size-self.y), (self.size+self.z))
        glTexCoord2f(1.0, 1.0); glVertex3f(-(self.size-self.x), (self.size+self.y), (self.size+self.z))
        glTexCoord2f(0.0, 1.0); glVertex3f(-(self.size-self.x), (self.size+self.y), -(self.size-self.z))
        glEnd()
    
    # Calculate vertices of the cube
    def calcVertices(self):
        # Vertices of the cube
        self.vertices = (
            ((self.size+self.x), -(self.size-self.y), -(self.size-self.z)),
            ((self.size+self.x), (self.size+self.y), -(self.size-self.z)),
            (-(self.size-self.x), (self.size+self.y), -(self.size-self.z)),
            (-(self.size-self.x), -(self.size-self.y), -(self.size-self.z)),
            ((self.size+self.x), -(self.size-self.y), (self.size+self.z)),
            ((self.size+self.x), (self.size+self.y), (self.size+self.z)),
            (-(self.size-self.x), -(self.size-self.y), (self.size+self.z)),
            (-(self.size-self.x), (self.size+self.y), (self.size+self.z))
        )

        # Edges of the cube
        self.edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
        )

        self.surfaces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6)
        )