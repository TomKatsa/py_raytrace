from SceneBuilder import SceneBuilder
from phys import *


w = 400
h = 200

back1 = (0, 0, 0)
back2 = (1, 1, 1)



# Defining sphere 1:
sph1_center = Vec3(0, 0.25, 1)
sph1_ambient = Vec3(1, 1, 0) # Yellow
sph1 = Sphere(sph1_center, 0.4, sph1_ambient)
# Defining sphere 2:
sph2_center = Vec3(0, 0, 1)
sph2_ambient = Vec3(0.3, 0.7, 1) # Blue
sph2 = Sphere(sph2_center, 0.6, sph2_ambient)

# Defining sphere 3:
sph3_center = Vec3(0, 0.1, 1)
sph3_ambient = Vec3(0, 1, 0)
sph3 = Sphere(sph3_center, 0.5, sph3_ambient)

# Defining sphere 4:
sph4_center = Vec3(0, 0.4, 1)
sph4_ambient = Vec3(1, 0.2, 0)
sph4 = Sphere(sph4_center, 0.3, sph4_ambient)

eye = Vec3(0, 0, 0)
scene = [sph4,sph1, sph3, sph2, sph4]
light_source = Vec3(1, 0, -0.4) # Light-source position


img = SceneBuilder(w, h, scene, light_source, back2, back1, eye)
img.show()