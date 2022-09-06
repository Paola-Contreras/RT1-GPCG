import numpy as np
import math_lib as ml 

WHITE = (1,1,1)
BLACK = (0,0,0)

#Point of contact 
class Intersect(object):
    def __init__(self, distance, point, normal, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObj = sceneObj

class Material(object):
    #diffuse is use only to put some color 
    def __init__(self, diffuse = WHITE):
        self.diffuse = diffuse


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = ml.subtract(self.center, orig)
        tca = ml.dot(L, dir)
        #d_norm = ml.normalized(L)
        #d= ((ml.power(d_norm,2)) - tca ** 2 )**0.5
        d = ( np.linalg.norm(L) ** 2 - tca ** 2) ** 0.5


        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
            
        # P = O + t0 * D
        mul = []
        for j in range(len(dir)):
            res = t0 * dir[j]
            mul.append(res)
        

        P = ml.add(orig, mul)
        normal = ml.subtract(P, self.center)
        normal = ml.normalized(normal)

      
        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self)