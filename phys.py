import math

class Vec3:
	#x, y, z = 0, 0, 0
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, vec):
		return Vec3(self.x + vec.x, self.y + vec.y, self.z + vec.z)
	def __sub__(self, vec):
		return Vec3(self.x - vec.x, self.y - vec.y, self.z - vec.z)
	def __mul__(self, num):
		return Vec3(self.x * num, self.y * num, self.z * num)
	def __truediv__(self, num):
		return Vec3(self.x / num, self.y / num, self.z / num)


	# Normalizing (unit vector): returning the vector divided by its magnitude.
	def normalize(self):
		mag = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		if mag == 0:
			return self
		div = 1 / mag
		return Vec3(self.x * div, self.y * div, self.z * div)

	def magnitude(self):
		return math.sqrt(self.x**2, self.y**2, self.z**2)

# Dot product of 2 vectors
def dot(v1, v2):
	return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)


class Ray:
	def __init__(self, o, d):
		self.o = o # Origin
		self.d = d.normalize() # Direction
		# Type: Vec3
	def point(self, t):
		return (self.o + self.d*t)


class Sphere:
	def __init__(self, center, r, ambient):
		self.center = center # Center (Vec3)
		self.r = r # Radius (value)
		self.ambient = ambient # Ambient color (Vec3)
		#self.refl = refl
		self.type = "Sphere"
	def intersect(self, ray):
		oc = ray.o - self.center
		direction = ray.d
		a = dot(direction, direction)
		b = 2 * dot(oc, direction)
		c = dot(oc, oc) - self.r**2
		discr = b*b - 4*a*c
		if discr < 0:
			return -1
		else:
			t1 = (-b + math.sqrt(discr)) / (2*a)
			t2 = (-b - math.sqrt(discr)) / (2*a)
			return t2



class Plane:
	def __init__(self, normal, ambient):
		self.normal = normal # Normal vector
		self.type = "Plane"
		self.ambient = ambient # Ambient color (Vec3)
		#self.refl = refl
	def intersect(self, ray):
		n = self.normal
		denom = dot(n, ray.d)
		if denom > 0.001:
			dsa = ray.d - ray.o
			t = dot(dsa, n)
			return t
		return -1





#Linearly blends two colors, determined by a scalar
def Blend(y, c1, c2):
	r = y*c1[0] + (1-y)*c2[0]
	g = y*c1[1] + (1-y)*c2[1]
	b = y*c1[2] + (1-y)*c2[2]
	return Vec3(r, g, b)



# Returns tuple for color
def Color(vec):
	#vec.z = vec.z/2 + 1
	#vec.z = vec.z**10
	col = vec*255
	return (int(col.x), int(col.y), int(col.z))



# Useless
def Depth(vec):
	z = vec.z**2
	z = z*200
	return (int(z), int(z), int(z))