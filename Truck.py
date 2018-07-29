from Vehicle import Vehicle

class Truck(Vehicle):

	max_load = 0
	speed_limit = 0

	def __init__(self, max_load, speed_limit, name, wheels, speed, weight, mileage, color):
		self.max_load = max_load
		self.speed_limit = speed_limit
		Vehicle.__init__(self, name, wheels, speed, weight, mileage, color, )
	
	def load(self):
		print("Truck is being loaded.")

	def unload(self):
		print("Truck is being unloaded.")

	def blocking_road(self):
		print("Move, Truck")
