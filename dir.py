import os 
def create(name,mode='a'):
 file=open(name ,mode)
 file.close()
create(input('enter file name '))
print(os.getcwd())


