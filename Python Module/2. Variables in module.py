#A module is a code library
#A file containing a set of funbctions that we wnat to include

# myModule.py is module we have created in this folder


#Now lets import myModule.py in this file
import myModule

#we can access variables of all types that are defined in a module
#here we are accessing a dictionary that is defined in myModule.py 
x = myModule.car1["color"]
print(x)