
f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f1 = open('filetwo.txt', 'w+')
f1.write("TWO FILE")
f1.close()


import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
