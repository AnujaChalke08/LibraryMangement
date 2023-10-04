from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
#setting tkinter window size
screen.geometry("%dx%d" % (width, height))
screen.title('Library Mangement systen')

# image2 = Image.open("backfinal (3).png")
# test = ImageTk.PhotoImage(image2)
#
# label2 = Label(image=test)
# label2.image = test
#
# label2.place(x=0, y=0)

def BookReg():
    bid = Bid_info.get()
    title = title_info.get()
    author = author_info.get()
    status = status_info.get()

    conn = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='Librarymang')
    curr = conn.cursor()

    # Your SQL query to insert data into the table
    sql_query = "INSERT INTO Library (Bid, title, author, status) VALUES (%s, %s, %s, %s)"

    # Data to be inserted into the database
    data = (bid, title, author, status)
    messagebox.showinfo("Success", 'Registration Successful')

    try:
        # Execute the query with the user input data
        curr.execute(sql_query, data)

        # Commit the transaction
        conn.commit()

        print("Data inserted successfully!")

    except mysql.connector.Error as err:
        # Handle any errors that occur during the insertion
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        curr.close()
        conn.close()






Label(screen, text="Add Book", font="Georgia 35 bold", bg="purple", fg="white").pack(fill="both")

Label(screen, text="BId", font="Verdana 25").place(x=330, y=120)
Label(screen, text="Title", font="Verdana 25").place(x=330, y=190)
Label(screen, text="Author", font="Verdana 25").place(x=330, y=260)
Label(screen, text="Status", font="Verdana 25").place(x=330, y=330)

# entry
Bid_info = StringVar()
title_info = StringVar()
author_info = StringVar()
status_info = StringVar()

Bid_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="Bid_info")
Bid_entry.place(x=800, y=120)
title_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="title_info")
title_entry.place(x=800, y=190)
author_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="author_info")
author_entry.place(x=800, y=260)
status_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="status_info")
status_entry.place(x=800, y=330)

register_btn = Button(screen, text="Register", font="Georgia 23 bold", height=1, width=10, fg='purple')
register_btn.place(x=600, y=500)
register_btn.configure(command=BookReg)





screen.mainloop()