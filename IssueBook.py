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

def Issue():
    Bid = Bid_info.get()
    IssueTo = Issue_info.get()

    Library = "Library"
    issueTable = "IssueBook"
    allBid = []

    con = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='Librarymang')
    cur = con.cursor()
    query = "select Bid from Library"
    try:
        cur.execute(query)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if Bid in allBid:
            checkAvail = "select status from " + Library + " where Bid = '" + Bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Can't fetch Book IDs")
    except:
        messagebox.showinfo("Error","Book ID not present" )

        issueSql = "insert into " + issueTable + " values ('" + Bid + "','" + IssueTo + "')"
        show = "select * from " + issueTable

        updateStatus = "update " + Library + " set status = 'issued' where bid = '" + Bid + "'"
        try:
            if Bid in allBid and status == True:
                cur.execute(issueSql)
                con.commit()
                cur.execute(updateStatus)
                con.commit()
                messagebox.showinfo('Success', "Book Issued Successfully")
                screen.destroy()
            else:
                allBid.clear()
                messagebox.showinfo('Message', "Book Already Issued")
                screen.destroy()
                return
        except:
            messagebox.showinfo("Search Error", "The value entered is wrong, Try again")
        print(Bid)
        print(IssueTo)

        allBid.clear()




Label(screen, text="Issue the Book", font="Georgia 35 bold", bg="purple", fg="white").pack(fill="both")

Label(screen, text="Book ID", font="Verdana 25").place(x=330, y=200)
Label(screen, text="Issued To", font="Verdana 25").place(x=330, y=300)

Bid_info = StringVar()
Issue_info = StringVar()

Bid_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="age_info")
Bid_entry.place(x=800, y=200)
Issue_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="phoneNo_info")
Issue_entry.place(x=800, y=300)

Issue_btn = Button(screen, text="Issue", font="Georgia 23 bold", height=1, width=10, fg='purple')
Issue_btn.place(x=400, y=500)
Issue_btn.configure(command=Issue)

Quit_btn = Button(screen, text="Quit", font="Georgia 23 bold", height=1, width=10, fg='purple')
Quit_btn.place(x=700, y=500)
Quit_btn.configure(command=Quit)




screen.mainloop()