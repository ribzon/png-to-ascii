from PIL import Image

# Set the width and height of the ASCII art
ASCII_WIDTH = 80
ASCII_HEIGHT = 80

# Open the PNG image using the PIL library
image = Image.open("image.png")

# Resize the image to the desired width and height
image = image.resize((ASCII_WIDTH, ASCII_HEIGHT))

# Convert the image to grayscale
image = image.convert("L")

# Get the pixel values of the image
pixels = list(image.getdata())

# Convert the pixel values to ASCII characters based on their brightness
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Convert each pixel to an ASCII character based on its brightness
ascii_art = ""
for i in range(len(pixels)):
    pixel = pixels[i]
    ascii_char = ascii_chars[int((pixel/255)*(len(ascii_chars)-1))]
    ascii_art += ascii_char
    if (i+1) % ASCII_WIDTH == 0:
        ascii_art += "\n"

# Print the ASCII art
print(ascii_art)
