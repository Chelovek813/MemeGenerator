from PIL import Image, ImageDraw, ImageFont

print("Meme generator launched!")
top_text = input("Enter top text: ")
bottom_text = input("Enter the text below: ")
print(f"{top_text} {bottom_text}")
print("List of images: ")
print("1. Cat in restaurant ")
print("2. Cat in glasses😎")
image_number = int(input("Enter number of the image: "))
if image_number == 1:
    image_file = "butercat.png"
elif image_number == 2:
    image_file = "krutoycat.png"



image = Image.open(image_file)
width, height = image.size


draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=70)
text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]
draw.text(((width - text_width) / 2, 10), top_text, font=font, fill='black')
text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]
draw.text(((width - text_width) / 2, height - text_height -10), bottom_text, font=font, fill='black')
image.save('Meme.png')