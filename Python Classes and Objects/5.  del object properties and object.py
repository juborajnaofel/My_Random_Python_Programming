class Car:
	def __init__(c,wheels,color):
		c.wheels = wheels
		c.color = color
	def fun(abc):
		print("Car color is: "+ abc.color)
car_1 = Car(4,"Red")
print("Car1: "+"Wheels = "+str(car_1.wheels)+", Color = "+str(car_1.color))

#Now lets delete the color property
del car_1.color
#The color property is deleted from car_1 object and now
#if you try to access it you will get an error


#Now lets delete the car_1 object
del car_1
#and it is deleted!