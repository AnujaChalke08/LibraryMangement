from tkinter import *
from tkinter import messagebox

import mysql.connector
from PIL import Image, ImageTk


# image2 = Image.open("backfinal (3).png")
# test = ImageTk.PhotoImage(image2)
#
# label2 = Label(image=test)
# label2.image = test
# label2.place(x=0, y=0)
screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
# setting tkinter window size
screen.geometry("%dx%d" % (width, height))
screen.title('Library Mangement systen')
Canvas1 = Canvas(screen)
# Canvas1.config(bg="#12a4d9")
Canvas1.pack(expand=True, fill=BOTH)
headingFrame1 = Frame(screen, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
labelFrame = Frame(screen, bg='black')
labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'),
        bg='black', fg='white').place(relx=0.07, rely=0.1)
Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
        fg='white').place(relx=0.05, rely=0.2)

con = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='Librarymang')
cur = con.cursor()
bookTable = "library"


def View():
    y = 0.25

    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

quitBtn = Button(screen, text="Quit", font="Georgia 23 bold", height=1, width=10, fg='purple', command=screen.destroy)
quitBtn.place(x=600, y=640)

screen.mainloop()


