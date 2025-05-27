"""Imports"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import floor

"""---Question 2---"""

I = Image.open("fonddecarte.png")
img = np.array(I)
plt.imshow(img)

"""---Question 4---"""

def conversion(lat, lon):
    return (lat, lon)

plt.plot()

plt.show()