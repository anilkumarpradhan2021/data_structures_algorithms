from abc import ABC,abstractclassmethod

"""
Abstract class for motor type
"""
class Motor(ABC):
	def drive(self):
		print("I am driving , ",self.__class__)
	
	@abstractclassmethod
	def number_of_wheels(self):
		pass

	
"""
Define the Bus implementation
"""	
class Bus(Motor):
	def number_of_wheels(self):
		print("I have 12 wheels")

"""
Define the Car implementation
"""	

class Car(Motor):
	def number_of_wheels(self):
		print("I have 4 wheels")


"""
Define the Motor Factory , so that user does not need to know about the actual Car / Bus implementation
"""	

class Motor_Factory():
	def create_motor(self,type):
		if type == "bus":
			return Bus()
		elif type == "car":
			return Car()	

if __name__ == "__main__":
	motor = Motor_Factory()
	motor.create_motor("bus").number_of_wheels()
	motor.create_motor("bus").drive()
				
	motor.create_motor("car").number_of_wheels()
	motor.create_motor("car").drive()
