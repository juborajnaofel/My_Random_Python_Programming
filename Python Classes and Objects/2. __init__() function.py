#just like a constructor it is used to assign values to object properties or
#other operations while creating an object of any class
class Car:
	#the parameter 'c' is a reference to the current instance of the class
	#and is used to access variables that belong to the class
	def __init__(c,wheels,color):
		c.wheels = wheels
		c.color = color
car_1 = Car(4,"Red")
car_2 = Car(6,"Blue")

print("Car1: "+"Wheels = "+str(car_1.wheels)+", Color = "+str(car_1.color))
print("Car2: "+"Wheels = "+str(car_2.wheels)+", Color = "+str(car_2.color))