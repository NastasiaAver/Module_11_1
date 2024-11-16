import emoji #Библиотека позволяет выделить яркий эмодзи
from PIL import Image #Позволяет обрабатывать картинки
import matplotlib.pyplot as plt #Создает наглядный график по нужным размерам
import numpy as np

def is_quality(filename):

    with Image.open(filename) as img:
        img.load()
        print(img.size)
        if img.size >= (1200, 800):
            print(result)
            gray_img = img.convert("L")
            gray_img.show()
            fig, ax = plt.subplots()
            ax.plot([1200, img.size[0]], [800, img.size[1]])
            plt.show()

        else:
            print(":thumbs_down: Try to get another picture")


result =emoji.emojize('Quality is :thumbs_up:')
is_quality("building.jpg")