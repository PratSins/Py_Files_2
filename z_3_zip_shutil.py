import shutil

dir2zip = 'D:\\C++ Files'

output_filename = 'Example'

k = shutil.make_archive(output_filename,'zip',dir2zip)
print(k)

shutil.unpack_archive('Example.zip', 'final_unzip','zip')