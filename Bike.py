from Vehicle import Vehicle

class Bike(Vehicle):
	
	handle = 0
	is_gear = 0

	def __init__(self, handle, is_gear, name, wheels, speed, weight, mileage, color):
		self.handle = handle
		self.is_gear = is_gear
		super().__init__(name, wheels, speed, weight, mileage, color)

	def wheelie(self):
		print("Bike is Doing a wheeeeeeelie!")

	def stoppee(self):
		print("Bike is doing a stoppee!")
