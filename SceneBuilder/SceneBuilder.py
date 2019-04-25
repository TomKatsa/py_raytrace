from phys import *
from PIL import Image
# import math

# w = 400
# h = 200
# ar = w / h

# Screen:
# (x=-1,y=-1)---------------------------------------------- (x=1,y=-1)
# -                                                       -
# -                                                       -
# -                                                       -
# -                         (0,0,0)                       -
# -                                                       -
# -                                                       -
# (x=-1,y=1)----------------------------------------------- (x=1, y=1)
# 
# Colors: (R:0-1, G:0-1, B:0-1)
# Eye: Target position (looking at <eye> position)







def Trace(ray, scene, depth, light_source, back):
	for sph in scene:
		t = sph.intersect(ray)
		if t>0.00001:
			hitPoint = ray.point(t)
			if sph.type == "Sphere":
				normal = (hitPoint - sph.center).normalize()
			else:
				normal = sph.normal

			light_vec = light_source - hitPoint
			intensity = dot(light_vec, normal)
			pxColor = Color(sph.ambient * intensity)
			return pxColor
		else:
			#back1 = back[0]
			#back2 = back[1]
			#light_blue = (0.3, 0.7, 1)
			#white = (1, 1, 1)
			background = Blend(ray.d.y, back[0], back[1])
			pxColor = Color(background)
	return pxColor


def SceneBuilder(w, h, scene, light_source, background1, background2, look_at):
	ar = w / h
	#look_at = Vec3(0, -1, -1) # Origin of the ray
	eye = Vec3(ar, 1, -1)/2 # Camera position
	plot = Image.new("RGB", (w, h))
	px = plot.load()
	for i in range(w):
		for j in range(h):
			x = i/w # X between 0 and 1
			y = j/h # Y between 0 and 1
			direction = Vec3(x*ar, y, 0) # Scale X by aspect ratio to match X and Y
			ray = Ray(look_at, direction - eye)
			back = [background1, background2]
			px[i, j] = Trace(ray, scene, 0, light_source, back)
	return plot






