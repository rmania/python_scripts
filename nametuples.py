from collections import namedtuple

#RGB color values
color = (55,155,255) # normal tuple

# dictionary
color = {'red': 55, 'green': 155, 'blue': 255}

Color = namedtuple("color", ["red", "green", "blue"])
color = Color(red=55, green=155, blue=255)

print(color.red)

