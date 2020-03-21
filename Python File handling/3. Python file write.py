#to overwrite use mode "w" or to append use "a"
file = open("write.txt","w")
str = input("Write something to the file:")
file.write(str)
file.close()

#now lets check our file by reading it
file = open("write.txt","r")
print("File content: "+file.read())
file.close()
