#a function calling itself is called recursion is a common mathematical and programming concept
def factorial_using_recursion(n):
	if n==0:
		return 1
	else:
		return n*factorial_using_recursion(n-1)
value = int(input("Enter a number:"))

if(value<0):
	print("Negative number isn't allowed")
else:
	x = factorial_using_recursion(value)
	print("Factorial of "+ str(value)+" is "+ str(x))