from tkinter import *
from  PIL import ImageTk, Image
import random


#adding images
dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]


#window
root = Tk()
title = root.title("Rolling Dice")
geometry = root.geometry("500x500")


#image label
img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
lab1 =Label(root, image=img)
lab1.image=img
lab1.pack()


#function to roll a dice
def roll():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    lab1.configure(image=img)
    lab1.image = img


button = Button(root, text="Roll a dice", command=roll).pack()          #to call roll function
button_quit = Button(root, text="Quit", command=root.destroy).pack()    #to quit window
root.mainloop()