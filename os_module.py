import os
import shutil

f = open( "practice.txt", 'w+') # it will create the file if it doesn't exist
f.write('This is a test string')
f.close()

print(os.getcwd())
print()

print(os.listdir())
print()

print(os.listdir("D:\\TXT files"))

print( shutil.move('practice.txt',"D:\\TXT files" ) ) # moves the practice.txt file to 2nd location
#********** will give **error** if file already exists at destination
# It is not necessary to use shutil.move in print()
