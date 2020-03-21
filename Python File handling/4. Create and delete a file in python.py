import os


#create a file, it will return error if the file exits
file = open("create a file.txt","x")
file.close()

#use "w" , if you want to create a file if it doesn't exist
value = int(input("Enter '1' to delete the file(Recommended):"))
#delete a file
if(value==1):
	os.remove("create a file.txt")
else:
	print("file is not deleted")
	


#to delete a folder use
#os.rmdir("foldername")