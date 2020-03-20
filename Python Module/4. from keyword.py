#import only parts from a module
from myModule import car1

#do not use myModule.car1, use car1
x = car1["color"]
print(x)