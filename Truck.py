from Vehicle import Vehicle

class Truck(Vehicle):

	max_load = 0
	speed_limit = 0

	def __init__(self, max_load, speed_limit, name, wheels, speed, weight, mileage, color):
		self.max_load = max_load
		self.speed_limit = speed_limit
		super().__init__(name, wheels, speed, weight, mileage, color, )
	
	def load():
		print("Truck is being loaded.")

	def unload():
		print("Truck is being unloaded.")

	def blocking_road():
		print("Move, Truck")
