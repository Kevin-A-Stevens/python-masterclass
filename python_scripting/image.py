from PIL import Image, ImageFilter

img = Image.open("./pikachu.jpg")
print(img) # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x7F44429C1040>
print(img.format)  # JPEG
print(img.size) # (640, 640)
print(img.mode)  # RGB
print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)  # SMOOTH, SHARPEN
filtered_img.save("blur.png", 'png')  # png supports the above image filters

converted_img = img.convert("L")
converted_img.save("grey.png", "png")

converted_img.show()  # shows image in new window
crooked = converted_img.rotate(90)
crooked.save("crooked.png", "png")
resize = converted_img.resize((300, 300))  # must be a tuple
resize.save("resize.png", "png")

box = (100, 100, 400, 400)
region = converted_img.crop(box)
region.save("crop.png", "png")

# Use thumbnail to create a profile picture
spaceman = Image.open("./spaceman.jpg")
print(spaceman.size) # (572, 302)
spaceman.thumbnail((200, 200)) # keeps aspect ratio. Modified current image
spaceman.save("thumbnail.jpg")  # looks squished
print(spaceman.size) # (200, 106)







