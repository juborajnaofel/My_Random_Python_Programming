#just like a constructor it is used to assign values to object properties or
#other operations while creating an object of any class
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
p1 = Person("")