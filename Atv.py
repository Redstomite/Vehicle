from Vehicle import Vehicle
from Bike import Bike
from Car import Car

class Atv(Bike, Car):
	
#	handle = None
#	has_belt = 0
#	is_gear = 0 
#	has_audioplayer = None

	def __init__(self, handle , is_gear , has_belt , has_audioplayer , has_ac , has_strwheel , name, wheels, speed, weight, mileage, color):
		Bike.__init__(self, handle, is_gear , name, wheels, speed, weight, mileage, color)
		Car.__init__(self, has_ac, has_strwheel, has_belt, has_audioplayer, name, wheels, speed, weight, mileage, color)
		

	def offroad(self):
		print("Leaving a dust trail!")
	
