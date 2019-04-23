from phys import *
from PIL import Image
# import math

w = 1920
h = 1080
ar = w / h



def Trace(ray, scene, depth):
	for sph in scene:
		t = sph.intersect(ray)
		if t>0.00001:
			hitPoint = ray.point(t)
			if sph.type == "Sphere":
				normal = (hitPoint - sph.center).normalize()
			else:
				normal = sph.normal

			light_pos = Vec3(0.5, -1, 0)
			light_vec = light_pos - hitPoint
			intensity = dot(light_vec, normal)
			pxColor = Color(sph.ambient * intensity)
			return pxColor
		else:
			pxColor = (255, 255, 255)
			light_blue = (0.3, 0.7, 1)
			white = (1, 1, 1)
			background = Blend(ray.d.y, white, light_blue)
			pxColor = Color(background)
	return pxColor


def main():
	plot = Image.new("RGB", (w, h))
	px = plot.load()
	light_blue = (0.3, 0.7, 1)
	white = (1, 1, 1)
	look_at = Vec3(0, 0, 0) # Origin of the ray
	eye = Vec3(ar, 1, -1)/2 # Camera position
	sph1_center = Vec3(0, 0.1, 1)
	sph1_ambient = Vec3(0, 1, 0)
	sph1 = Sphere(sph1_center, 0.5, sph1_ambient)
	pl1_norm = Vec3(0, 1, 0)
	pl1_ambient = Vec3(0, 0, 1)
	pl1 = Plane(pl1_norm, pl1_ambient)
	#scene = [sph1, pl1]
	scene = [sph1]
	for i in range(w):
		for j in range(h):
			x = i/w # X between 0 and 1
			y = j/h # Y between 0 and 1
			direction = Vec3(x*ar, y, 0) # Scale X by aspect ratio to match X and Y
			ray = Ray(look_at, direction - eye)
			px[i, j] = Trace(ray, scene, 0)
	plot.show()
	plot.save("Example.png")
	plot.save("Example.bmp")




main()
