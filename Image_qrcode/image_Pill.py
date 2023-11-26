from PIL import Image, ImageDraw, ImageFont

# my_image = Image.open("D:\IT dars\photo_2023-11-04_13-59-26.jpg")

# my_image.load()
# my_image.save("Messi.jpg")
# print(my_image.format, my_image.size)


img = Image.new("RGBA", (640, 640), "white")
font = ImageFont.truetype("arial.ttf", size=50)
draw = ImageDraw.Draw(img)
draw.text((200, 200), text="Hello world!", fill="yellow", font=font)
img.show()

