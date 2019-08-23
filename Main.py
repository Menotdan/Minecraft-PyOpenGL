# Image loader with PIL
import ImageLoader
# Cube object
from Models.Cube import Cube
# For making a window and for user input
import pygame
from pygame.locals import *
# For rendering 3D
from OpenGL.GL import *
from OpenGL.GLU import *
# For frame timings
import time
# For randomness
import random
# Width and height
disp_width = 960
disp_height = 600
frames = 0
time1 = 0
time2 = 0
total = 0
fps = 0
textureIDs = []
spd = 0.1

textureNames = [
    "Grass_Top",
    "Stone_Block"
]

def loadTextures():
    # Configure vars
    global textureNames
    pos = 0
    tempIDs = []
    # For every texture in the list of names, load that file from the textures directory and assign an ID for it
    for name in textureNames:
        ID = glGenTextures(1)
        img_data = ImageLoader.load("Textures/" + name + ".png")
        tempIDs.append((ID, name))
        glBindTexture(GL_TEXTURE_2D, ID)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(
            GL_TEXTURE_2D, 0, 3, img_data[0], img_data[1], 0,
            GL_RGBA, GL_UNSIGNED_BYTE, img_data[2]
        )
    return tempIDs

def selectTextureByID(id):
    # Select texture as the active texture
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glBindTexture(GL_TEXTURE_2D, id)

def selectTextureByName(name):
    global textureIDs
    # Find texture
    for t in textureIDs:
        if t[1] == name:
            # Found Texture! Select it as the active texture
            glEnable(GL_TEXTURE_2D)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
            glBindTexture(GL_TEXTURE_2D, t[0])
            return None

def main():
    # Variables
    global frames
    global time1
    global time2
    global total
    global fps
    global textureIDs

    moveTowards = True
    paused = False
    run = True
    up_down_angle = 0

    # Initialize pygame
    pygame.init()
    display = (disp_width, disp_height)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    # Camera perspective
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    # Position camera
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    glRotatef(0,0,0,0)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()
    # Enable Depth
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    # Lighting
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    # Load all the textures 
    textureIDs = loadTextures()

    # Initialize the cube objects
    cubes = []
    for x in range(10):
        for y in range(10):
            for z in range(10):
                cubes.append(Cube(x-5, y-5, z-5-20, 0.5))
    # Setup pygame dependent variables
    displayCenter = [display[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)
    while run:
        # Allow pausing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    paused = not paused
                    pygame.mouse.set_pos(displayCenter) 
            if not paused: 
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pygame.mouse.set_pos(displayCenter)    

        if not paused:
            # get keys
            keypress = pygame.key.get_pressed()
            #mouseMove = pygame.mouse.get_rel()

            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1]*0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # init the view matrix
            glPushMatrix()
            glLoadIdentity()

            # apply the movment 
            if keypress[pygame.K_w]:
                glTranslatef(0,0,spd)
            if keypress[pygame.K_s]:
                glTranslatef(0,0,-spd)
            if keypress[pygame.K_d]:
                glTranslatef(-spd,0,0)
            if keypress[pygame.K_a]:
                glTranslatef(spd,0,0)
            if keypressp[pygame.K_LSHIFT]:
                glTranslatef(0,-spd,0)

            # apply the left and right rotation
            glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

            # multiply the current matrix by the get the new view matrix and store the final vie matrix 
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            # Clear the OpenGL buffers
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            # Draw cubes
            start = time.time()
            for c in cubes:
                selectTextureByID(random.randint(1,2))
                c.draw()
            stop = time.time()
            print("Took " + str(stop-start) + " to render large cube")
            glRotatef(1, random.randint(1,3), random.randint(1,3), random.randint(1,3))
            glPopMatrix()

            # Update display and delay
            pygame.display.flip()
            pygame.time.wait(10)
            if frames == 0:
                time1 = time.time()
            frames += 1
            if frames == 60:
                time2 = time.time()
                total = time2 - time1
                fps = frames / total
                frames = 0
                print("Current FPS: " + str(fps))


# Begin the main loop
main()