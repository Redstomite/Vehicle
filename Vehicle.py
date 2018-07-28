class Vehicle():

	name = None
	wheels = 0
	speed = 0
	weight = 0
	mileage = 0
	color = None

	def __init__(self, name, wheels, speed, weight, mileage, color):
		self.name = name
		self.wheels = wheels
		self.speed = speed
		self.weight = weight
		self.mileage = mileage
		self.color = color

	def go_forward(dist):
		loc = loc+dist
		print("Current location is : " + str(dist))

	def reverse(dist):
		loc = loc-dist
		print("Current location is : " + str(dist))
	def stop():
		print("All stop.")
