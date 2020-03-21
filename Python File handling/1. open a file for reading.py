#open(filename, mode) 


#to open a file for reading
file = open("samplefile.txt")
print(file.read())

#[same as above]to open a file for reading
file = open("samplefile.txt","rt")
#whole txt content will be returned
print(file.read())

print("==========================================================================")

#Read only Parts of the file..Return as much characters as you want
file = open("samplefile.txt","rt")
#this will print first 2 characters
print(file.read(2))
#this will print the characters start after the previous read() returns
print(file.read(3))
print("==========================================================================")

#read lines
file = open("samplefile2.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

#close a file
file.close()
