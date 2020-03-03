import pyautogui
from tkinter import*

welcome = Tk()
welcome.title('SCREENSHOT')
welcome.geometry("300x300")

def save():
    x = nameofimg.get()
    takeScreenshot(x)

def takeScreenshot (x):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(x)

nameofimg = Entry(welcome)
nameofimg.insert(0, '.jpg')
nameofimg.place(height=20, x=100,y=100)

mybutton = Button(welcome, text= "take screenshot", command= save, bg='green', fg='white', font=10)
mybutton.place(height=30, x=100, y=150)

welcome.mainloop()