def another_func():
	#python definition can't be empty
	#so "pass" keyword could be used to avoid error
	#a funtion with no content could be written;  a "pass" statement in it to avoid errors
	pass
def main(x):
	str = "Hey"
	return str*x
x = main(1)
print(x)
x =main(2)
print(x)
x = main(5)
print(x)