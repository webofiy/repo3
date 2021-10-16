# crud opreation using python file handling 
#1 crating emty file 
file =open("dev.txt","a")
file.close()
# appending data
file =open("dev.txt","a+")
data =input ("enter your info here ")
file.write(data)
file.close()
# reading data 
file =open("dev.txt","r")
print(file.read())
file.close()

