# Introduction

'''
Do you pronounce it “GIF” or a “JIF”? Either way, Graphics Interchange Format (GIF) is great for creating animated images. The format has been around since 1987 and helped define the early internet. It’s used to display memes, graphics, logos, and it's everywhere — on websites, text messages, and social media.

GIFs are “animated images” because they aren’t exactly videos. They are more like flipbooks; they don’t have sound and flip through multiple pictures sequentially. 🎞️
'''

import imageio.v3 as iio

filenames = ['1.png', '2.png']

images = []

for filenames in filenames:
    images.append(iio.imread(filenames))
    iio.imwrite('me.gif', images, duration = 500, loop = 0)
    
#Runnning the program: go the terminal navigate the folder with the python file using cd, put cd Projects
# Run python3 create_gif.py
    
    
    
    
    





