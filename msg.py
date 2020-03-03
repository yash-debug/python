from tkinter import *
from tkinter import messagebox

welcome = Tk()
welcome.title('Signup page')
welcome.geometry("800x800")
def click():
    messagebox.showinfo('INFO.', 'SIGNUP SUCCESSFUL')

head = Label(welcome, padx=20, text="REGISTRATION FORM :", fg = "red", font = "Helvetica 25 bold")
head.grid(pady=25)

name = Label(welcome, text="NAME :- ", font="bold")
name.grid(row=3, column=0, pady=20)

name_field = Entry(welcome)
name_field.insert(0, 'FIRST')
name_field.grid(row=3 , column=1, padx=25)

name_fiel = Entry(welcome)
name_fiel.insert(0, 'LAST')
name_fiel.grid(row=3 , column=2)

email = Label(welcome, text="EMAIL :- ", font="bold")
email.grid(row=4, column=0, pady=15)

email_field = Entry(welcome)
email_field.insert(0, '@gmail.com')
email_field.grid(row=4 , column=1)

phone = Label(welcome, text="PHONE :- ", font="bold")
phone.grid(row=5, column=0, pady=20)

phone_field = Entry(welcome)
phone_field.insert(0, '+91')
phone_field.grid(row=5 , column=1)

address = Label(welcome, text="ADDRESS :- ", font="bold")
address.grid(row=6, column=0, pady=30)

address_field = Text(welcome, height=3, width=20)
address_field.grid(row=6, column=1)

gender = Label(welcome, text="GENDER :-", font="bold")
gender.grid(row=8, column=0, pady=30)

gender_field = Radiobutton(welcome, text="Male", value=1)
gender_field.grid(row=8, column=1)
gender_field1 = Radiobutton(welcome, text="Female", value=2)
gender_field1.grid(row=8, column=2)

title = Label(welcome, text="TITLE :-", font="bold")
title.grid(row=9, column=0, pady=40)
title_field = Entry(welcome)
title_field.grid(row=9, column=1)

workshop = Label(welcome, text="WORKSHOP PACKAGE", font="bold")
workshop.grid(row=10, column=0)
workshop_field = Radiobutton(welcome, text="Begginer", value=1)
workshop_field.grid(row=10, column=1)
workshop_field1 = Radiobutton(welcome, text="Pro", value=2)
workshop_field1.grid(row=10, column=2)



btn = Button(welcome, text="ENTER", fg='cyan', bg='red', command=click)
btn.place(height=30, x=100, y=600)

welcome.mainloop()