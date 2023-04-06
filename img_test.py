from PIL import Image

mac = Image.open('img1.jpg')
print("type(mac) ->",type(mac))
print("mac ->",mac)
mac.show() # opens the image
print("mac.size ->",mac.size)

print("mac.filename ->",mac.filename)

print("mac.format_description ->",mac.format_description)

# mac.crop() --> pass a tuple to make it work
k = mac.crop((0,0,100,100))
# the 1st two are the starting point and the rest two are width and height, rightwards and downwards repectively
print(k)



#mac.paste(im=k,box=(0,100))-- didnt work