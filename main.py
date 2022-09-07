from gl import Raytracer, V3
from figures import *
from light import *


width = 900
height = 900

# Materiales

orange = Material(diffuse = (1,0.5,0))
black = Material(diffuse = (0, 0, 0))
white = Material(diffuse = (1,1,1))
red = Material(diffuse = (1,0,0))


rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

#Body of the snowman
rtx.scene.append( Sphere(V3(0,-3,-10), 2, white) )
rtx.scene.append( Sphere(V3(0,0,-10), 1.5, white) )
rtx.scene.append( Sphere(V3(0,2.3,-10), 1, white) )

# #Buttons 
rtx.scene.append( Sphere(V3(0,-1.5,-6), 0.30, black) )
rtx.scene.append( Sphere(V3(0,-0.6,-6), 0.25, black) )
rtx.scene.append( Sphere(V3(0,0.2,-6), 0.20, black) )

# #Face
rtx.scene.append( Sphere(V3(0,1.7,-7), 0.1, orange) )
rtx.scene.append( Sphere(V3(0,1.4,-7), 0.08, black) )
rtx.scene.append( Sphere(V3(0.2,1.43,-7), 0.08, black) )
rtx.scene.append( Sphere(V3(-0.2,1.43,-7), 0.08, black) )
rtx.scene.append( Sphere(V3(-0.2,1.9,-7), 0.11, black) )
rtx.scene.append( Sphere(V3(0.2,1.9,-7), 0.11, black) )
rtx.scene.append( Sphere(V3(0.16,1.35,-5), 0.02, white) )
rtx.scene.append( Sphere(V3(-0.16,1.35,-5), 0.02, white) )

rtx.glRender()

rtx.glFinish("output.bmp")