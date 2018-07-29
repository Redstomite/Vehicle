from Vehicle import Vehicle

class Car(Vehicle):
	
	has_ac = None
	has_strwheel = None
	has_belt = 0
	has_audioplayer = None

	def __init__(self, has_ac, has_strwheel, has_belt, has_audioplayer, name, wheels, speed, weight, mileage, color):
		self.has_ac = has_ac
		self.has_strwheel = has_strwheel
		self.has_belt = has_belt
		self.has_audioplayer = has_audioplayer
		Vehicle.__init__(self, name, wheels, speed, weight, mileage, color)
	
	def drift(self):
		print("Drifting - Wheee!")

	def deploy_airbags(self):
		print("Crash!")

