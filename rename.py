import os

os.chdir('/Users/Mike/Desktop/photo')   # Change to your folder

i = 1

for f in os.listdir():

    new_name = str(i) + '.jpg'  # Change to your file type

    i += 1

    os.rename(f, new_name)
