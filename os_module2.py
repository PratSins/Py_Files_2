import os
import shutil
import send2trash

f = open( "practice2.txt", 'w+') # it will create the file if it doesn't exist
f.write('This is a test string')
f.close()

send2trash.send2trash('practice2.txt')


####################################################################################################################

#  >> os.unlink(path) - which deletes a file at the path your provide
#  >> os.rmdir(path) - which deletes a folder (folder must be empty) at the path your provide
#  >> shutil.rmtree(path) - this is the most dangerous, as it will remove all files and folders contained in the path. All of these
#                           methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead
#                           we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of
#                           permanent removal.

#     Install the send2trash module with
#         pip install send2trash
