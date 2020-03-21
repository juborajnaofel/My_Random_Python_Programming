#read a whole file line by line
file = open("samplefile2.txt","r")
for a in file:
	print(a)
#close a file
file.close()
