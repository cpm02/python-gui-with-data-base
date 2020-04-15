from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root=Tk()

root.geometry("1000x1000")
canvas=Canvas(root,width=1000,height=1000)
image =ImageTk.PhotoImage(Image.open('lib.jpg'))
canvas.create_image(0,0,anchor=NW,image=image )
canvas.pack()
#_________________database_____________________
text1=StringVar()
text2=StringVar()
text3=StringVar()
text4=StringVar()
text5=StringVar()
text6=IntVar()
text7=IntVar()


def submit():
    bookid=text1.get()
    bookname=text2.get()
    author=text3.get()
    genre=text4.get()
    edition=text5.get()
    cost=text6.get()
    quantity=text7.get()

    conn = sqlite3.connect('project.db')
    with conn:
       cursor = conn.cursor()
       cursor.execute('INSERT INTO book VALUES (?, ?, ?, ?, ?, ?, ?)',(bookid,bookname,author,genre,edition,cost,quantity,))
       

    
def show():
  connt = sqlite3.connect('project.db')
  with connt:
    cursor = connt.cursor()
    cursor.execute("SELECT * FROM book ")
    rows=cursor.fetchall()
    for row in rows:
        box.insert(END,row,str(""))

#_____________________books_________________
Label(canvas,text='BookID',bg='white').place(x=10,y=10)
e1=Entry(canvas,textvar=text1).place(x=100,y=10)

Label(canvas,text='Name',bg='white').place(x=10,y=50)
e2=Entry(canvas,textvar=text2).place(x=100,y=50)

Label(canvas,text='Author',bg='white').place(x=10,y=90)
e3=Entry(canvas,textvar=text3).place(x=100,y=90)

Label(canvas,text='Genre',bg='white').place(x=10,y=130)
e4=Entry(canvas,textvar=text4).place(x=100,y=130)

Label(canvas,text='Edition',bg='white').place(x=10,y=170)
e5=Entry(canvas,textvar=text5).place(x=100,y=170)

Label(canvas,text='Cost',bg='white').place(x=10,y=210)
e6=Entry(canvas,textvar=text6).place(x=100,y=210)

Label(canvas,text='Quantity',bg='white').place(x=10,y=250)
e7=Entry(canvas,textvar=text7).place(x=100,y=250)


f1=Frame(canvas,bg="grey")
f1.place(x=350,y=10)
scroll=Scrollbar(f1)
scroll.pack(side=RIGHT,fill=Y)

box=Listbox(f1,height=20,width=60)
box.pack()


box.config(yscrollcommand=scroll.set)
scroll.config(command=box.yview)
    





#________________Button_____________________
add=Button(canvas,text='Add',command=submit).place(x=10,y=300)
show=Button(canvas,text='Show',command=show).place(x=60,y=300)
delete=Button(canvas,text='Delete').place(x=110,y=300)
home=Button(canvas,text='Home').place(x=160,y=300)



mainloop()

