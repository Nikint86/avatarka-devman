from PIL import Image
monro = Image.open("monro.jpg")
red, green, blue = monro.split()
coordinates = (50, 0, red.width, red.height)
red_cut = red.crop(coordinates)
red_cut2 = red.crop((25,0,671, red.height))
red_smesh = Image.blend(red_cut, red_cut2, 0.5)
coordinates = ((25,0,671, blue.height))
blue_cut = blue.crop(coordinates)
coordinates = ((0,0,646, blue.height))
blue_cut2 = blue.crop(coordinates)
blue_smesh = Image.blend(blue_cut, blue_cut2, 0.5)
coordinates = ((25,0,671, green.height))
green_cut = green.crop(coordinates)
monro_final = Image.merge("RGB", (red_smesh, green_cut, blue_smesh))
monro_final.thumbnail((80, 80)) 











