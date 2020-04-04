from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("400x680")
root.title("Calculator")
root.configure(bg = "black")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar = scvalue, font = "lucida 40 bold", background = "white")
screen.pack(fill = X, padx = 20, pady = 20, )

f = Frame(root, bg = "black", borderwidth = "2", relief = RAISED)
b = Button(f, text = "7", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "8", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "9", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

f.pack()

f = Frame(root, bg = "black", borderwidth = "2", relief = RAISED)
b = Button(f, text = "4", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "5", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "6", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

f.pack()

f = Frame(root, bg = "black", borderwidth = "2", relief = RAISED)
b = Button(f, text = "1", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "2", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "3", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

f.pack()

f = Frame(root, bg = "black", borderwidth = "2", relief = RAISED)
b = Button(f, text = "0", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "-", font = "lucida 28 bold", padx = 12)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "+", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

f.pack()

f = Frame(root, bg = "black", borderwidth = "2", relief = RAISED)
b = Button(f, text = "/", font = "lucida 28 bold", padx = 14)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "%", font = "lucida 28 bold", padx = 1)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = ".", font = "lucida 28 bold", padx = 14)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

f.pack()

f = Frame(root, bg = "black", borderwidth = "2", relief = RAISED)
b = Button(f, text = "*", font = "lucida 28 bold", padx = 12)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "C", font = "lucida 28 bold", padx = 4)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

b = Button(f, text = "=", font = "lucida 28 bold", padx = 8)
b.pack(side = LEFT, padx = 15, pady = 5)
b.bind("<Button -1>", click)

f.pack()

root.mainloop()
