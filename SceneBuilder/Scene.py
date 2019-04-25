from phys import *
from SceneBuilder import SceneBuilder

w = 400
h = 200


light_blue = (0.3, 0.7, 1) # Background color 1
white = (1, 1, 1) # Background color 2


# Defining sphere 1:
sph1_center = Vec3(0.6, 0.1, 1)
sph1_ambient = Vec3(0, 1, 0) # Green
sph1 = Sphere(sph1_center, 0.5, sph1_ambient)
# Defining sphere 2:
sph2_center = Vec3(0, 0.1, 1)
sph2_ambient = Vec3(1, 0, 0) # Red
sph2 = Sphere(sph2_center, 0.4, sph2_ambient)
# Defining sphere 3:
sph3_center = Vec3(-0.5, 0, 1)
sph3_ambient = Vec3(0.54, 0.17, 0.89) # Purple
sph3 = Sphere(sph3_center, 0.6, sph3_ambient)
scene = [sph2, sph1, sph3]
light_source = Vec3(0.75, -1, 0) # Light-source position

eye = Vec3(0, 0, 0)


img = SceneBuilder(w, h, scene, light_source, white, light_blue, eye)
img.show()