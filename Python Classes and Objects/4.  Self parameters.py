class Car:
	# parameter 'c' is a 'self' parameter 
	# you can use the name 'self' or any other name for this parameter
	def __init__(c,wheels,color):
		c.wheels = wheels
		c.color = color
	#abc is also refering to 'self' so we can use any name.
	def fun(abc):
		print("Car color is: "+ abc.color)
car_1 = Car(4,"Red")
print("Car1: "+"Wheels = "+str(car_1.wheels)+", Color = "+str(car_1.color))

#Now lets access that function
car_1.fun()