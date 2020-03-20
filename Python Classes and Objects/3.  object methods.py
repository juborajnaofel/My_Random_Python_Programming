class Car:
	def __init__(c,wheels,color):
		c.wheels = wheels
		c.color = color
	#we can also define functions for classes
	def fun(c):
		print("Car color is: "+ c.color)
car_1 = Car(4,"Red")
print("Car1: "+"Wheels = "+str(car_1.wheels)+", Color = "+str(car_1.color))

#Now lets access that function
car_1.fun()