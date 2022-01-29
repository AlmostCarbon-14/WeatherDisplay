from tkinter import *
import os
from Scraper import *

try:
    from PIL import ImageTk, Image
except:
    os.system("python3 -m pip install --upgrade pip")
    os.system("python3 -m pip install --upgrade Pillow")
imagePath = os.path.dirname(os.path.realpath(__file__)) + "\\Images\\"


class Display:

    def __init__(self):
        self.lunarPhase = handleLunarData()
        self.weatherData = handleWeatherData()
        self.window = Tk()
        self.canvas = Canvas(self.window, width=300, height=300, bg='black')
        self.canvas.pack()
        self.weatherImg = ImageTk.PhotoImage(Image.open(imagePath + "weatherImg.png").convert("RGB"))
        self.moonImg = ImageTk.PhotoImage(Image.open(imagePath + "moonPhase.jpg").convert("RGB"))
        self.canvas.create_image(80, 80, anchor=NW, image=self.weatherImg)
        self.canvas.create_image(80, 80, anchor=SW, image=self.moonImg)
        self.window.mainloop()


disp = Display()
