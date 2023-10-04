import os
from tkinter import *

import mysql.connector
from tkinter import messagebox

screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
#setting tkinter window size
screen.geometry("%dx%d" % (width, height))
screen.title('Library Mangement systen')



def Quit():
    os.system("LibraryMang.py")

def Return():
    screen.bid = Bid_info.get()
    screen.Return = fees_info.get()

    IssueTo = "IssueTo"
    bookTable = "Library"
    allBid = []

    if (int(screen.Return) >= 500):
        messagebox.showerror("error", "please enter Fees below 100")


    con = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='Librarymang')
    cur = con.cursor()

    extractBid = "select bid from " + IssueTo
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if screen.bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + screen.bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Can't fetch Book IDs")
    except:
        messagebox.showinfo("Error","Book ID not present" )




Label(screen, text="Return Book", font="Georgia 35 bold", bg="purple", fg="white").pack(fill="both")

Label(screen, text="Book ID", font="Verdana 25").place(x=330, y=200)
Label(screen, text="Fees", font="Verdana 25").place(x=330, y=300)

Bid_info = StringVar()
fees_info = StringVar()


Bid_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="Bid_info")
Bid_entry.place(x=800, y=200)
fees_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="fees_info")
fees_entry.place(x=800, y=300)


Return_btn = Button(screen, text="Return", font="Georgia 23 bold", height=1, width=10, fg='purple')
Return_btn.place(x=400, y=400)
Return_btn.configure(command=Return)

Quit_btn = Button(screen, text="Quit", font="Georgia 23 bold", height=1, width=10, fg='purple')
Quit_btn.place(x=700, y=400)
Quit_btn.configure(command=Quit)



screen.mainloop()