class ExampleClass:
	#x is a property
	x = 2
#creating objects of that class
o1 = ExampleClass()
print("When obj1 created: " + str(o1.x))
o1.x = 3
print("When obj1 changed:" + str(o1.x))

#creating another object of that class
o2 = ExampleClass()
print("-----------------------------------------------");
print("Now printing both objects x property:")
print("Obj1.x: "+str(o1.x))
print("Obj2.x: "+str(o2.x))