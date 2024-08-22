from PIL import Image
example = Image.open("example.jpg")
lenna = Image.open("lenna.jpg")
monro = Image.open("monro.jpg")
red = Image.open("red.jpg")
red_cut = Image.open("red_cut.jpg")
blue = Image.open("blue.jpg")
green = Image.open("green.jpg")
print("Ширина -", example.width)
print("Высота -", example.height)
print("Цветовая модель -", example.mode)
print("Ширина -", lenna.width)
print("Высота -", lenna.height)
print("Цветовая модель -", lenna.mode)
lenna_RGB = lenna.convert("RGB")
print("Цветовая модель -", lenna_RGB.mode)
red, green, blue = monro.split()
blue.save("blue.jpg")
red.save("red.jpg")
green.save("green.jpg")
red_cut2 = Image.open("red.jpg")
new_monro = Image.merge("RGB", (red, green, blue))
new_monro.save("new_monro.jpg")
print(red.size)
coordinates = (50, 0, red.width, red.height)
red_cut = red.crop(coordinates)
red_cut.save("red_cut.jpg")
red_cut2 = red.crop((25,0,671, red.height))
red_cut2.save("red_cut2.jpg")
red_smesh = Image.blend(red_cut, red_cut2, 0.5)
red_smesh.save("red_smesh.jpg")
coordinates = ((25,0,671, blue.height))
blue_cut = blue.crop(coordinates)
blue_cut.save("blue_cut.jpg")
coordinates = ((0,0,646, blue.height))
blue_cut2 = blue.crop(coordinates)
blue_cut2.save("blue_cut2.jpg")
blue_smesh = Image.blend(blue_cut, blue_cut2, 0.5)
blue_smesh.save("blue_smesh.jpg")
coordinates = ((25,0,671, green.height))
green_cut = green.crop(coordinates)
green_cut.save("green_cut.jpg")
monro_final = Image.merge("RGB", (red_smesh, green_cut, blue_smesh))
monro_final.save("monro.final.jpg")
monro_final.thumbnail((80, 80)) 
print(monro_final.size)
monro_final.save("monro.final.jpg")











