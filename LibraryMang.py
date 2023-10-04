import os
from tkinter import *
from PIL import Image, ImageTk

screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
#setting tkinter window size
screen.geometry("%dx%d" % (width, height))
screen.title('Library Mangement systen')

image2 = Image.open("libraryImage (2).jpg")
test = ImageTk.PhotoImage(image2)

label2 = Label(image=test)
label2.image = test

label2.place(x=0, y=0)

Label(screen, text="Welcome To My Library", font="Georgia 35 bold").pack(fill="both")

def Book():
    os.system('Book.py')

def AddBook():
    os.system('AddBook.py')

def IssueBook():
    os.system('IssueBook.py')

def ReturnBook():
    os.system('ReturnBook.py')

Book_btn = Button(screen, text="Book View", font="Georgia 18 bold underline", height=2, width=20, bd=0)
Book_btn.place(x=500, y=250)
Book_btn.configure(command=Book)

AddBook_btn = Button(screen, text="Add Book", font="Georgia 18 bold underline", height=2, width=20, bd=0)
AddBook_btn.place(x=500, y=350)
AddBook_btn.configure(command=AddBook)

Issue_btn = Button(screen, text="Issue Book", font="Georgia 18 bold underline", height=2, width=20, bd=0)
Issue_btn.place(x=500, y=450)
Issue_btn.configure(command=IssueBook)

Return_btn = Button(screen, text="Return Book", font="Georgia 18 bold underline", height=2, width=20, bd=0)
Return_btn.place(x=500, y=550)
Return_btn.configure(command=ReturnBook)



screen.mainloop()