import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import *
import webbrowser
import random
import smtplib
import datetime
from PIL import Image,ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
#Your Changes Here
mydb = mysql.connector.connect(host='localhost', user='''Your Mysql user name''', password='''Your Sql Password''', database='''Your database Name''')
# Database Schema present In Schema Structure Folder.
cur = mydb.cursor()


# Function for random ID for Registration
def f():
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    bk = "REGI"
    c_ = random.choice(a)
    d_ = random.choice(a)
    e_ = random.choice(a)
    f_ = random.choice(a)
    g_ = random.choice(a)
    k = '@' + bk + str(c_) + str(d_) + str(e_) + str(f_) + str(g_)
    return k

def BookId():
    c=0
    for i in range(1,6):
        a=[1,2,3,4,5,6,7,8,9]
        c=(c*10)+random.choice(a)
    return"@BOOK"+str(c)

def OTP():
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    c_ = random.choice(a)
    d_ = random.choice(a)
    e_ = random.choice(a)
    f_ = random.choice(a)
    g_ = random.choice(a)
    h_ = random.choice(a)
    k =  str(c_) + str(d_) + str(e_) + str(f_) + str(g_) + str(h_)
    return k

root = tk.Tk()
root.geometry("1000x450+500+230")
root.resizable(False,False)
root.title("MAIN LOGIN")
root.configure(bg="white")
l2=tk.Label(root,text="LIBRARY MANAGEMENT",bg="white",font=('Arial',25,'bold')).place(x=430,y=10)

image=Image.open("chitkara.png").resize((500,300))
photo=ImageTk.PhotoImage(image)

label1 = tk.Label(root,bg="white",image=photo)
label1.pack(side="left")

f1 = tk.Frame(root, height=70,bg="white", width=200)
f1.place(x=580,y=110)

image2=Image.open("CU_logo.png").resize((400,350))
photo2=ImageTk.PhotoImage(image2)
l3=Label(text="Created By - Dhruv Seth, Deepankar Garg",bg="white").place(x=600,y=400)

def BEbook():
    win1=Toplevel(root)
    cur.execute('select Sno,book from ebooks')
    b = cur.fetchall()
    win1.geometry("650x390+670+250")
    win1.resizable(False,False)
    win1.configure(bg="#82AAE3")
    win1.title("OPEN A Ebook")

    f1=tk.Frame(win1,bg="orange")
    f1.pack(pady=20,padx=10)


    trv = ttk.Treeview(f1, selectmode='browse',height=8)
    trv.grid(row=0,column=0,sticky="ew")
    def open():
        try:
            select=trv.selection()[0]
            Sel1='select * from ebooks where Sno = %s'
            a__=[select]
            cur.execute(Sel1,a__)
            Data1=cur.fetchall()
            b__=Data1[0][2]
            print(b__)
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new(b__)
        except:
            win9=Toplevel(root)
            win9.geometry("350x200+740+420")
            win9.configure(bg="white")
            win9.resizable(False,False)
            l1=Label(win9,text="YOUR SELECTION IS EMPTY",bg="white",font=("ARIAL 12 bold")).pack(pady=40,padx=10)
            b1=Button(win9,text="RETRY",bg='cyan',width=10,command=win9.destroy).pack(pady=10,padx=10)


    b1 = tk.Button(win1,text="Open",width=20,bg="white",command=open).place(x=150,y=315)
    b2 = tk.Button(win1, text="Exit", width=20, bg="white", command=win1.destroy).place(x=350,y=315)
    # style
    style=ttk.Style()
    # style.theme_use("clam")
    style.configure('Treeview',
                    background="#BFEAF5",
                    forecolor="black",
                    rowheight=30,
                    fieldcolor="#BFEAF5")
    style.configure('Treeview.Heading',backgound="green")
    style.map('Treeview',
              background=[('selected','orange')])
    # end of style

    trv["column"] = ("1", "2")
    trv["show"] = "headings"


    trv.column("1", width=150, anchor='c')
    trv.column("2", width=390, anchor='c')
    trv.heading("1", text="Sno")
    trv.heading("2", text="NameOfBook")

    for i in b:
        trv.insert("", 'end', iid=i[0], values=(i[0], i[1]))
    trv_scroll = ttk.Scrollbar(f1, orient="vertical", command=trv.yview)
    trv_scroll.grid(row=0, column=1, sticky="ns")
    trv["yscrollcommand"] = trv_scroll.set
    win1.mainloop()


def admin():
    win1= Toplevel(root)
    win1.geometry("600x450+600+250")
    win1.resizable(False,False)
    win1.configure(bg="#E5FDD1")
    win1.title("The Admin Window")
    user_name = tk.StringVar()

    def my_fun(*args):
        cur.execute("select * from libEmail")
        lib=cur.fetchall()
        lib_=lib[0][1]
        if lib_=='':
            win11=Toplevel(root)
            win11.geometry('600x200')
            win11.configure(bg="#E5FDD1")
            Em_=StringVar()
            def B11():
                a_="update libEmail set Email = %s where Email = ''"
                b_=[Em_.get()]
                cur.execute(a_,b_)
                mydb.commit()
                win11.destroy()
                Em_.set("")
                win12 = Toplevel(root)
                win12.geometry("400x150+900+350")
                l1 = Label(win12, text="YOUR EMAIL IS REGISTERED", font=("ARIAL 13 bold")).pack(padx=20, pady=10)
                b1 = Button(win12, text="EXIT", width=15, command=win12.destroy).pack(pady=10)

            L4 = tk.Label(win11, text="Enter the Email: ", font=("ARIAL", 12, "bold"), bg="#E5FDD1")
            L4.place(x=60, y=50)
            E4 = tk.Entry(win11, width=30, textvariable=Em_)
            E4.place(x=280, y=50)
            E4.focus()
            B11 = tk.Button(win11, text="Add Email", width=20, command=B11)
            B11.place(x=100, y=120)
            B12 = tk.Button(win11, text="Exit", width=20, command=win11.destroy)
            B12.place(x=300, y=120)
        else:
            win12=Toplevel(root)
            win12.geometry("350x170")
            OTP15_=StringVar()
            win12.configure(bg="#E5FDD1")

            def SEND_OTP():
                global b_
                cur.execute("select * from libemail")
                a_ = cur.fetchall()
                V1 = a_[0][1]
                b_ = str(OTP())
                # Email
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('''  "Enter The Admin Email"  ''', ''''  "Enter Password for Admin gmail"  ''')
                msg = 'Hello,Your OTP is ' + str(b_)
                server.sendmail('''  "Enter The Admin Email"  ''', V1, msg)  # ("sender","reciever","msg")
                server.close()
                # end of email

            def Submit():
                if OTP15_.get() == b_:
                    win19 = Toplevel(root)
                    win19.geometry("500x200+550+350")
                    win19.configure(bg="#AAE3E2")
                    l1 = Label(win19, text="ENTER NEW PASSWORD ", font=("ARIAL", 10, "bold"), bg="#AAE3E2")
                    l1.place(x=50, y=40)
                    l1 = Label(win19, text="CONFIRM PASSWORD", font=("ARIAL", 10, "bold"), bg="#AAE3E2")
                    l1.place(x=50, y=88)
                    y__ = StringVar()
                    z__ = StringVar()
                    E1 = Entry(win19, width=20, textvariable=y__).place(x=280, y=40)
                    E2 = Entry(win19, width=20, textvariable=z__).place(x=280, y=90)
                    win12.destroy()

                    def B1():
                        y_ = y__.get()
                        z_ = z__.get()
                        if y_ != '':
                            if z_ != '':
                                if y_ == z_:
                                    x = "update password set pass = %s where name ='pa'"
                                    w = [y_]
                                    cur.execute(x, w)
                                    mydb.commit()
                                    y__.set("")
                                    z__.set("")
                                    win19.destroy()
                                else:
                                    I1 = Toplevel(win19)
                                    I1.geometry("250x130+900+440")
                                    l1 = Label(I1, text="NEW PASSWORD DOES NOT MATCH THE CONFIRM PASSWORD").pack(pady=10,padx=15)
                                    b1 = Button(I1, text="Retry", width=10, bg='#AAE3E2', command=I1.destroy).pack(pady=10)
                            else:
                                I2 = Toplevel(win19)
                                I2.geometry("3500x130+900+440")
                                l2 = Label(I2, text="CONFIRM PASSWORD IS EMPTY").pack(pady=10)
                                b2 = Button(I2, text="Retry", width=10, bg='#AAE3E2', command=I2.destroy).pack(pady=10)
                        else:
                            I3 = Toplevel(win19)
                            I3.geometry("220x130+900+440")
                            l3= Label(I3, text="NEW PASSWORD IS EMPTY").pack(pady=10)
                            b3 = Button(I3, text="Retry", width=10, bg='#AAE3E2', command=I3.destroy).pack(pady=10)

                    b1 = Button(win19, text="Submit", width=10, bg="white", command=B1).place(x=180, y=140)

            L1 = Label(win12, text="Enter The OTP", bg="cyan").place(x=30, y=40)
            E1 = Entry(win12, width=20, textvariable=OTP15_).place(x=150, y=40)
            B1 = Button(win12, width=10, text="SEND OTP", bg="white", command=SEND_OTP).place(x=15, y=100)
            B2 = Button(win12, width=10, text="SUBMIT", bg="white", command=Submit).place(x=130, y=100)
            B3 = Button(win12, width=10, text="EXIT", bg="white", command=win12.destroy).place(x=245, y=100)

    L1 = tk.Label(win1, text="Enter the Password: ",font=("ARIAL",15,"bold"),bg="#E5FDD1")
    L1.place(x=30,y=100)
    E1 = tk.Entry(win1, width=17, textvariable=user_name,font=('ARIAL 15'))
    E1.place(x=320,y=102)
    E1.focus()
    L3=tk.Label(win1,text="FORGET PASSWORD?",fg='Blue',bg="#E5FDD1",font=('ARIAL',10,'underline'))
    L3.place(x=360,y=225)
    L3.bind("<Button-1>",my_fun)

    def B1(*args):
        cur.execute("select * from password where name = 'pa'")
        b__ = cur.fetchall()
        c = b__[0][1]
        d=user_name.get()
        if c==d:
            win1.destroy()
            win3 = Toplevel(root)
            win3.geometry("1250x750+360+110")

            win3.title("Choose Between The ADMIN OPTIONS")
            win3.resizable(False, False)

            def B1():
                mydb = mysql.connector.connect(host='localhost', user='root', password='@Behappy12',database='librarymanagement')
                cur = mydb.cursor()

                win5 = Toplevel(root)

                win5.geometry("900x480+540+300")
                win5.resizable(False,False)
                win5.title("Issue Book")
                win5.configure(bg="#B9F3FC")

                l2 = tk.Label(win5, text="ISSUE A BOOK", bg="#B9F3FC", font=('Arial', 25, 'bold')).place(x=330, y=10)

                f1 = tk.Frame(win5)
                f1.configure(bg="#B9F3FC")
                f1.pack(side="left", anchor="n", padx=30, pady=60)
                f2 = tk.Frame(win5)
                f2.configure(bg="#B9F3FC")
                f2.pack(side="left", anchor="n", padx=30, pady=60)
                f3 = tk.Frame(win5)
                f3.configure(bg="#B9F3FC")
                f3.pack(side="left", anchor="n", padx=50, pady=70)

                cur.execute("select * from pbooks")
                b = cur.fetchall()
                trv = ttk.Treeview(f3, selectmode='browse', height=12)
                trv.grid(row=0, column=0, sticky="ew")

                # style
                style = ttk.Style()
                # style.theme_use("clam")
                style.configure('Treeview',
                                background="#BFEAF5",
                                forecolor="black",
                                rowheight=22,
                                fieldcolor="#BFEAF5")
                style.configure('Treeview.Heading', backgound="green")
                style.map('Treeview',
                          background=[('selected', 'orange')])
                # end of style


                trv["column"] = ("1", "2", "3")
                trv["show"] = 'headings'

                trv.column("1", width=100, anchor='c')
                trv.column("2", width=150, anchor='c')
                trv.column("3", width=100, anchor='c')

                trv.heading("1", text="Book Number")
                trv.heading("2", text="Books")
                trv.heading("3", text="Quantity")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2]))
                trv_scroll = ttk.Scrollbar(f3, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set


                # Message Box Missing
                a__ = tk.StringVar()
                b__ = tk.StringVar()
                c__ = tk.StringVar()
                d__ = tk.StringVar()
                e__ = tk.StringVar()

                l1 = tk.Label(f1, text="Enter Registration Number *", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l2 = tk.Label(f1, text="Enter the Book Number * ", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l3 = tk.Label(f1, text="Enter your Email *", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l4 = tk.Label(f1, text="Issue_Date YYYY-MM-DD *", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l5 = tk.Label(f1, text="Enter The Book Name *", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")

                E1 = tk.Entry(f2, textvariable=a__).pack(pady=20)
                E2 = tk.Entry(f2, textvariable=b__).pack(pady=20)
                E3 = tk.Entry(f2, textvariable=c__).pack(pady=20)
                E4 = tk.Entry(f2, textvariable=d__).pack(pady=20)
                E5 = tk.Entry(f2, textvariable=e__).pack(pady=20)
                def B13():
                    try:
                        select=trv.focus()
                        values=trv.item(select,'values')
                        b__.set(values[0])
                        e__.set(values[1])
                        now = datetime.datetime.now()
                        p = str(now)[0:10]
                        d__.set(p)
                    except:
                        now = datetime.datetime.now()
                        p = str(now)[0:10]
                        d__.set(p)
                        pass
                def B12():
                    a_ = "@REGI" + a__.get()
                    b_ = b__.get()
                    c_ = c__.get()
                    d_ = d__.get()
                    e_ = e__.get()
                    cur.execute("select * from registration")
                    bk = cur.fetchall()
                    for i in range(len(bk)):
                        if a_ == bk[i][0]:
                            if b_!='' and b_.isnumeric():
                                if c_!='' and c_[-10:]=="@gmail.com" or c_[-7:]==".edu.in":
                                    if d_[4]=='-' and d_[7]=='-' and len(d_)==10:
                                        N1 = bk[i][2]
                                        Id = BookId()
                                        Name1 = bk[i][1]
                                        q1 = "insert into student(Id,Name,Email,Phone_Number,Issue_Date,Name_of_Book_issued,Book_Number) values(%s,%s,%s,%s,%s,%s,%s)"
                                        V1 = [Id, Name1, c_, N1, d_, e_, b_]
                                        cur.execute(q1, V1)
                                        mydb.commit()
                                        Check1="select * from student where Id=%s"
                                        Check2=[a_]
                                        cur.execute(Check1,Check2)
                                        Check3 = cur.fetchall()
                                        mydb.commit()

                                        if 1:
                                            q2 = "update pbooks SET quantity=quantity-1 where Sno = %s"
                                            V2 = [b_]
                                            cur.execute(q2, V2)
                                            mydb.commit()

                                        server = smtplib.SMTP('smtp.gmail.com', 587)
                                        server.starttls()
                                        server.login("librarymg0123@gmail.com", "ypswfhklylhurbvm")
                                        msg = 'Hello,Your book ' + e_ + ' has been issued on ID ' + str(Id) + "on Date " +d_
                                        server.sendmail("librarymg0123@gmail.com", c_, msg)
                                        server.close()

                                        a__.set("")
                                        b__.set("")
                                        c__.set("")
                                        d__.set("")
                                        e__.set("")
                                        break
                                    else:
                                        I1 = Toplevel(win5)
                                        I1.geometry("220x130+900+440")
                                        l1 = Label(I1, text="Issue Date is INVALID").pack(pady=10,padx=15)
                                        b1 = Button(I1, text="Retry", width=10, bg='#AAE3E2', command=I1.destroy).pack(pady=10)
                                else:
                                    I1 = Toplevel(win5)
                                    I1.geometry("220x130+900+440")
                                    l1 = Label(I1, text="Book Number is Incorrect").pack(pady=10,padx=15)
                                    b1 = Button(I1, text="Retry", width=10, bg='#AAE3E2', command=I1.destroy).pack(pady=10)
                            else:
                                I2 = Toplevel(win5)
                                I2.geometry("220x130+900+440")
                                l2 = Label(I2, text="Book Number is Incorrect").pack(pady=10,padx=15)
                                b2 = Button(I2, text="Retry", width=10, bg='#AAE3E2', command=I2.destroy).pack(pady=10)
                    else:
                        I4 = Toplevel(win5)
                        I4.geometry("220x130+900+440")
                        l4 = Label(I4, text="Book Registration is Incorrect").pack(pady=10,padx=15)
                        b4 = Button(I4, text="Retry", width=10, bg='#AAE3E2', command=I4.destroy).pack(pady=10)


                    # end email
                    mydb.commit()
                b1 = tk.Button(win5, text="Submit", width=10,bg="white",command=B12).place(x=180, y=390)
                b2 = tk.Button(win5, text="INSERT", width=15, bg="white", command=B13).place(x=620, y=390)
                b3 = tk.Button(win5, text="Exit", width=10,bg="white",command=win5.destroy).place(x=320, y=390)
                win5 = mainloop()

            def B2():
                win8 = Toplevel(root)
                win8.geometry("2100x1000+0+0")
                win8.configure(bg="#AAE3E2")
                win8.attributes('-fullscreen',True)

                f1 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=5, height=70).pack(fill="x")
                f9 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=5, height=60).pack(fill='x', pady=1)
                B7=Button(win8,text="EXIT THE WINDOW",bg="white",height=3,width=30,command=win8.destroy).place(x=830,y=1000)

                # The Red Box
                f12 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=7, width=710, height=460)
                f12.place(x=1220, y=130)
                f2 = Frame(win8, bg="#AAE3E2")
                f2.place(x=1290, y=200)

                # The White Box
                f15 = Frame(win8, bg="#AAE3E2", width=610, height=342, relief=RIDGE, bd=7)
                f15.place(x=610, y=650)

                # The Grey Box
                f4 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=7, width=610, height=343)
                f4.place(x=0, y=650)

                # The Pink Box
                f13 = Frame(win8, bg="#AAE3E2", width=710, relief=RIDGE, bd=7, height=342)
                f13.place(x=1220, y=650)
                f3 = Frame(win8, bg="#AAE3E2")
                f3.place(x=1320, y=720)

                f5 = Frame(win8, bg="#AAE3E2", width=610, relief=RIDGE, bd=7, height=230).place(x=610, y=130)
                f6 = Frame(win8, bg="#AAE3E2", width=610, relief=RIDGE, bd=7, height=230).place(x=0, y=360)

                f7 = Frame(win8, bg="#AAE3E2", width=610, height=230, relief=RIDGE, bd=7, ).place(x=0, y=130)
                f8 = Frame(win8, bg="#AAE3E2", width=610, height=230, relief=RIDGE, bd=7, ).place(x=610, y=360)

                # Yhe All Box Frame
                f11 = Frame(win8, bg="#AAE3E2", width=1950, height=60, relief=RIDGE, bd=7)
                f11.place(x=0, y=590)

                l1 = Label(win8, text="CHANGE THE STOCK WINDOW", fg="Black", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l1.place(x=760, y=15)

                l2 = l1 = Label(win8, text="PHYSICAL BOOKS", fg="Black", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l2.place(x=860, y=82)

                l3 = Label(win8, text="Add a Book", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l3.place(x=210, y=140)
                l4 = Label(win8, text="Add Book Quantity ", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l4.place(x=770, y=140)
                l5 = Label(win8, text="Remove a Book ", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l5.place(x=180, y=370)
                l6 = Label(win8, text="Remove Book Quantity ", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l6.place(x=735, y=370)
                l7 = Label(win8, text="Physical Book Records ", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l7.place(x=1380, y=140)
                l8 = Label(win8, text="E-Book Records ", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l8.place(x=1450, y=670)
                l9 = l1 = Label(win8, text="PHYSICAL BOOKS", bg="#AAE3E2", fg="black", font=("Arial", 20, "bold"))
                l9.place(x=860, y=598)
                l10 = Label(win8, text="Add a Book ", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l10.place(x=210, y=660)
                l11 = Label(win8, text="Remove a Book ", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l11.place(x=800, y=660)

                # Label that Work

                # The Yellow Box

                l12 = Label(win8, text="Enter Book Name", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l12.place(x=100, y=195)

                l13 = Label(win8, text="Enter Book Quantity", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l13.place(x=100, y=240)
                a__ = StringVar()
                b__ = StringVar()
                E1 = Entry(win8, textvariable=a__, width=20)
                E1.place(x=350, y=198)

                E2 = Entry(win8, textvariable=b__, width=20)
                E2.place(x=350, y=242)

                def B1():
                    a_ = a__.get().upper()
                    b_ = b__.get()
                    if a_!='':
                        if b_!='' and b_.isnumeric():
                            q1 = "insert into pbooks(books,quantity) Values(%s,%s)"
                            V1 = [a_, b_]
                            cur.execute(q1, V1)
                            mydb.commit()
                            a__.set("")
                            b__.set("")
                        else:
                            I1=Toplevel(win8)
                            I1.geometry("220x130+990+440")
                            l1=Label(I1,text="Book Quantity is Incorrect").pack(pady=10)
                            b1=Button(I1,text="Retry",width=10,bg='#AAE3E2',command=I1.destroy).pack(pady=10)
                    else:
                        I2 = Toplevel(win8)
                        I2.geometry("220x130+990+440")
                        l2 = Label(I2,text="Book Name is Incorrect").pack(pady=10)
                        b2 = Button(I2,text="Retry",width=10,bg='#AAE3E2', command=I2.destroy).pack(pady=10)



                B1 = tk.Button(win8, text="Click To Add A Book",width=24,bg="white",command=B1).place(x=220, y=300)

                # The Orange Box

                l14 = Label(win8, text="Enter Book Number", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l14.place(x=700, y=195)

                l14 = Label(win8, text="Enter Book Quantity to Add", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l14.place(x=700, y=240)

                c__ = StringVar()
                d__ = StringVar()

                E3 = Entry(win8, textvariable=c__, width=20)
                E3.place(x=990, y=198)

                E4 = Entry(win8, textvariable=d__, width=20)
                E4.place(x=990, y=240)

                def B2():
                    c_ = c__.get()
                    d_ = d__.get()
                    if c_!='' and c_.isnumeric():
                        if d_!='' and d_.isnumeric():
                            q1 = "update pbooks SET quantity=quantity+%s where Sno= %s"
                            V2 = [d_, c_]
                            cur.execute(q1, V2)
                            mydb.commit()
                            c__.set("")
                            d__.set("")
                        else:
                            I3=Toplevel(win8)
                            I3.geometry("220x130+990+440")
                            l1=Label(I3,text="Book Quantity is Incorrect").pack(pady=10)
                            b1=Button(I3,text="Retry",width=10,bg='#AAE3E2',command=I3.destroy).pack(pady=10)
                    else:
                        I4 = Toplevel(win8)
                        I4.geometry("220x130+900+440")
                        l1 = Label(I4, text="Book Number is Incorrect").pack(pady=10)
                        b1 = Button(I4, text="Retry",width=10,bg='#AAE3E2', command=I4.destroy).pack(pady=10)

                B2 = tk.Button(win8, text="ADD BOOK QUANTITY",bg="white",width=24, command=B2).place(x=840, y=300)

                # The Blue Box
                l15 = Label(win8, text="Enter Book Number", font=("Arial", 14, "bold"), bg="#AAE3E2")
                l15.place(x=100, y=435)

                e__ = StringVar()

                E5 = Entry(win8, width=20, textvariable=e__)
                E5.place(x=350, y=442)

                def B3():
                    if e__.get()!='' and e__.get().isnumeric():
                        q3 = "delete from pbooks where Sno=%s"
                        e_ = e__.get()
                        V3 = [e_]
                        cur.execute(q3, V3)
                        mydb.commit()
                        e__.set("")
                    else:
                        I5 = Toplevel(win8)
                        I5.geometry("220x130+900+440")
                        l5 = Label(I5, text="Book Number is Incorrect").pack(pady=10)
                        b5 = Button(I5, text="Retry",width=10,bg='#AAE3E2', command=I5.destroy).pack(pady=10)

                B3 = tk.Button(win8, text="REMOVE A BOOK",bg="white",width=24,command=B3).place(x=220, y=530)

                # The light blue Box
                l16 = Label(win8, text="Enter Book Number", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l16.place(x=700, y=435)

                l17 = Label(win8, text="Enter Book Quantity", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l17.place(x=700, y=480)

                f__ = StringVar()
                g__ = StringVar()

                E12 = Entry(win8, width=20, textvariable=f__)
                E12.place(x=990, y=440)

                E7 = Entry(win8, width=20, textvariable=g__)
                E7.place(x=990, y=480)

                def B4():
                    f_ = f__.get()
                    g_ = g__.get()
                    if f_!='' and f_.isnumeric():
                        if g_ != '' and g_.isnumeric():
                            q4 = "update pbooks SET quantity=quantity-%s where Sno = %s"
                            V4 = [g_, f_]
                            cur.execute(q4, V4)
                            mydb.commit()
                            f__.set("")
                            g__.set("")
                        else:
                            I6 = Toplevel(win8)
                            I6.geometry("220x130+900+440")
                            l6 = Label(I6, text="Book quantity is Incorrect").pack(pady=10)
                            b6 = Button(I6, text="Retry",width=10,bg='#AAE3E2', command=I6.destroy).pack(pady=10)
                    else:
                        I7 = Toplevel(win8)
                        I7.geometry("220x130+900+440")
                        l7 = Label(I7, text="Book Number is Incorrect").pack(pady=10)
                        b7 = Button(I7, text="Retry",width=10,bg='#AAE3E2', command=I7.destroy).pack(pady=10)

                B4 = tk.Button(win8, text="REMOVE BOOK QUANTITY",width=24,bg="white",command=B4).place(x=840, y=530)

                # The Grey Box

                l18 = Label(win8, text="Name of Book", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l18.place(x=70, y=730)

                l19 = Label(win8, text="Enter Link", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l19.place(x=70, y=782)
                h__ = StringVar()
                i__ = StringVar()
                E9 = Entry(win8, width=35, textvariable=h__)
                E9.place(x=250, y=732)

                E10 = Entry(win8, width=35, textvariable=i__)
                E10.place(x=250, y=785)

                def B5():
                    h_ = h__.get().upper()
                    i_ = i__.get()
                    if h_!='':
                        if i_!='':
                            q5 = "insert into ebooks(book,link) values(%s,%s)"
                            V5 = [h_, i_]
                            cur.execute(q5, V5)
                            mydb.commit()
                            h__.set("")
                            i__.set("")
                        else:
                            I8 = Toplevel(win8)
                            I8.geometry("220x130+900+440")
                            l8 = Label(I8, text="Link is Invalid").pack(pady=10)
                            b8 = Button(I8, text="Retry",width=10,bg='#AAE3E2', command=I8.destroy).pack(pady=10)
                    else:
                        I9 = Toplevel(win8)
                        I9.geometry("220x130+900+440")
                        l9 = Label(I9, text="Book Name is Empty").pack(pady=10)
                        b9 = Button(I9, text="Retry",width=10,bg='#AAE3E2', command=I9.destroy).pack(pady=10)

                B5 = tk.Button(win8, text="ADD E-BOOK",width=24,bg="white",command=B5).place(x=220, y=880)

                # The white Box
                l20 = Label(win8, text="Enter Sno of Book", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l20.place(x=680, y=735)

                j__ = StringVar()

                E6 = Entry(win8, width=20, textvariable=j__)
                E6.place(x=990, y=740)

                def B6():
                    j_ = j__.get()
                    if j_!='':
                        q6 = "delete from ebooks where Sno = %s"
                        V6 = [j_]
                        cur.execute(q6, V6)
                        mydb.commit()
                        j__.set("")
                    else:
                        I10 = Toplevel(win8)
                        I10.geometry("220x130+900+440")
                        l10 = Label(I10, text="Book Sno is Empty or INVALID").pack(pady=10)
                        b10 = Button(I10, text="Retry",width=10,bg='#AAE3E2',command=I10.destroy).pack(pady=10)

                B6 = tk.Button(win8, text="REMOVE A E-BOOK",bg="white",width=25, command=B6).place(x=840, y=880)

                # All the entry widget

                cur.execute("select * from pbooks")
                b = cur.fetchall()
                trv = ttk.Treeview(f2, selectmode='browse', height=16)
                trv.grid(row=0, column=0, sticky="ew")


                # style
                style = ttk.Style()
                # style.theme_use("clam")
                style.configure('Treeview',
                                background="#BFEAF5",
                                forecolor="black",
                                fieldcolor="#BFEAF5")
                style.configure('Treeview.Heading', backgound="green")
                style.map('Treeview',
                          background=[('selected', 'orange')])
                # end of style



                trv["column"] = ("1", "2", "3")
                trv["show"] = 'headings'

                trv.column("1", width=100, anchor='c')
                trv.column("2", width=350, anchor='c')
                trv.column("3", width=100, anchor='c')

                trv.heading("1", text="Book Number")
                trv.heading("2", text="Books")
                trv.heading("3", text="Quantity")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2]))
                trv_scroll = ttk.Scrollbar(f2, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set

                # The E-books field

                cur.execute('select Sno,book from ebooks')
                b = cur.fetchall()

                trv = ttk.Treeview(f3, selectmode='browse', height=10)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2")
                trv["show"] = "headings"

                trv.column("1", width=150, anchor='c')
                trv.column("2", width=340, anchor='c')
                trv.heading("1", text="Sno")
                trv.heading("2", text="NameOfBook")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1]))
                trv_scroll = ttk.Scrollbar(f3, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set


            def B3():

                win13 = Toplevel(root)
                win13.geometry("700x300+650+350")
                win13.configure(bg="#B9F3FC")
                win13.resizable(False,False)
                a__ = StringVar()
                b__ = StringVar()
                def B11():
                    now = datetime.datetime.now()
                    p = str(now)[0:10]
                    b__.set(p)

                def B1():
                    a_ = "@BOOK" + a__.get()
                    z = a__.get()
                    b_ = b__.get()
                    cur.execute("select * from student")
                    bk = cur.fetchall()
                    if z!='' and z.isnumeric() and len(z)==5:
                        if b_!='' and b_[4]=='-' and b_[7]=='-' and len(b_)==10:
                            for i in range(len(bk)):
                                if a_ == bk[i][0]:
                                    q4 = "select Email from student where Id = %s"
                                    V4 = [a_]
                                    cur.execute(q4, V4)
                                    Email = cur.fetchall()
                                    Email_ = Email[0][0]
                                    q3 = "select Issue_Date from student where Id = %s"
                                    V3 = [a_]
                                    cur.execute(q3, V3)
                                    D_ = cur.fetchall()
                                    date_ = D_[0][0]
                                    DateT = b_
                                    k = date_.split('-')
                                    l = []
                                    for q in k:
                                        l.append(int(q))
                                    h_ = DateT.split('-')
                                    j = []
                                    for u in h_:
                                        j.append(int(u))
                                    date1 = datetime.date(l[0], l[1], l[2])
                                    date2 = datetime.date(j[0], j[1], j[2])
                                    dif = date2 - date1
                                    dy = dif.days
                                    if dy<=30:
                                        cur.execute("select * from student")
                                        bk = cur.fetchall()
                                        V1 = [bk[i][0]]
                                        q1 = "delete from student where Id=%s"
                                        cur.execute(q1, V1)
                                        mydb.commit()
                                        if 1:
                                            q2 = "update pbooks SET quantity=quantity+1 where Sno = %s"
                                            V2 = [bk[i][6]]
                                            cur.execute(q2, V2)
                                            mydb.commit()
                                            a__.set("")
                                            b__.set("")
                                        win22=Toplevel(win13)
                                        win22.geometry("450x150+640+260")
                                        win22.title("BOOK RETURNED")
                                        win22.configure(bg="#B9F3FC")

                                        server = smtplib.SMTP('smtp.gmail.com', 587)
                                        server.starttls()
                                        server.login("librarymg0123@gmail.com", "ypswfhklylhurbvm")
                                        msg = "YOUR BOOK IS RETURNED"

                                        server.sendmail("librarymg0123@gmail.com", Email_, msg)
                                        server.close()

                                        b2 = Button(win22, text="EXIT", width=13, height=2, bg="white",command=win22.destroy).place(x=150, y=75)
                                        l1 = Label(win22, text="YOUR BOOK IS RETURNED", bg="#B9F3FC",font=("ARIAL 15 bold")).place(x=70, y=20)

                                    else:
                                        Total_Money = str((dy-30)*2)
                                        def B2():
                                            cur.execute("select * from student")
                                            bk = cur.fetchall()
                                            V1 = [bk[i][0]]
                                            q1 = "delete from student where Id=%s"
                                            cur.execute(q1, V1)
                                            mydb.commit()
                                            if 1:
                                                q2 = "update pbooks SET quantity=quantity+1 where Sno = %s"
                                                V2 = [bk[i][6]]
                                                cur.execute(q2, V2)
                                                mydb.commit()
                                                A = 0
                                                win22 = Toplevel(win21)
                                                win22.geometry("450x140+640+260")
                                                win22.title("BOOK RETURNED")
                                                win22.configure(bg="#B9F3FC")
                                                b2 = Button(win22, text="EXIT", width=13, height=2, bg="white",command=win22.destroy).place(x=150, y=75)
                                                l1 = Label(win22, text="YOUR BOOK IS RETURNED", bg="#B9F3FC",font=("ARIAL 15 bold")).place(x=70, y=20)
                                                q4 = "select Email from student where Id = %s"
                                                V4 = [a_]
                                                cur.execute(q4, V4)
                                                Email = cur.fetchall()
                                                Email_ = Email[0][0]

                                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                                server.starttls()
                                                server.login("librarymg0123@gmail.com", "ypswfhklylhurbvm")
                                                msg = "YOUR BOOK IS RETURNED"
                                                server.sendmail("librarymg0123@gmail.com", Email_, msg)
                                                server.close()
                                                a__.set("")
                                                b__.set("")
                                        win21 = Toplevel(win13)
                                        win21.geometry("450x180+500+190")
                                        win21.configure(bg="#B9F3FC")
                                        b1 = Button(win21, text="SUBMIT", width=13, height=2, bg="white",command=B2).place(x=80, y=95)
                                        b2 = Button(win21, text="EXIT", width=13, height=2, bg="white",command=win21.destroy).place(x=220, y=95)
                                        l1 = Label(win21, text=Total_Money + "Rs - To be Paid \n2Rs Per Day, For late Submission",bg="#B9F3FC", font=("ARIAL 12 bold")).place(x=50, y=20)
                        else:
                            I2 = Toplevel(win13)
                            I2.geometry("220x130+900+400")
                            l2 = Label(I2, text="invalid Return Date").pack(pady=10)
                            b2 = Button(I2, text="Retry", command=I2.destroy).pack(pady=10)
                    else:
                        I2 = Toplevel(win13)
                        I2.geometry("220x130+900+400")
                        l2 = Label(I2,text="BOOK ID is INVALID or Empty").pack(pady=10)
                        b2 = Button(I2,text="Retry", command=I2.destroy).pack(pady=10)


                l1 = tk.Label(win13, text="ENTER BOOK ID", font=("arial", 15, "bold"), bg="#B9F3FC").place(x=30,y=40)
                E1 = tk.Entry(win13, width=25, textvariable=a__).place(x=440, y=45)
                l1 = tk.Label(win13, text="Enter Return Date YYYY-MM-DD", font=("arial", 15, "bold"), bg="#B9F3FC").place(x=30,y=120)
                E2 = tk.Entry(win13, width=25, textvariable=b__).place(x=440, y=125)

                b1 = Button(win13, text="Click to Return",width=20,bg="white", command=B1)
                b1.place(x=145, y=200)
                b2 = Button(win13, text="EXIT", bg="white",width=20, command=win13.destroy)
                b2.place(x=385, y=200)
                b2 = Button(win13, text="INSERT", bg="white", width=8, command=B11)
                b2.place(x=610, y=120)

            def B4():
                win4 = Toplevel(root)
                cur.execute("select * from student")
                b = cur.fetchall()
                win4.geometry("1200x420+340+250")
                win4.resizable(False, False)
                win4.configure(bg="#B9F3FC")
                win4.title("VIEW BOOK ISSUED")

                f1 = tk.Frame(win4, bg="orange")
                f1.pack(pady=20, padx=10)

                trv = ttk.Treeview(f1, selectmode='browse', height=12)
                trv.grid(row=0, column=0, sticky="ew")

                # style
                style = ttk.Style()
                # style.theme_use("clam")
                style.configure('Treeview',
                                background="#BFEAF5",
                                forecolor="black",
                                fieldcolor="#BFEAF5")
                style.configure('Treeview.Heading', backgound="green")
                style.map('Treeview',
                          background=[('selected', 'orange')])
                # end of style

                trv["column"] = ("1", "2", "3", "4", "5", "6","7")
                trv["show"] = 'headings'

                trv.column("1", width=120, anchor='c')
                trv.column("2", width=220, anchor='c')
                trv.column("3", width=250, anchor='c')
                trv.column("4", width=120, anchor='c')
                trv.column("5", width=120, anchor='c')
                trv.column("6", width=170, anchor='c')
                trv.column("7", width=140,anchor='c')
                trv.heading("1", text="Id")
                trv.heading("2", text="Name")
                trv.heading("3", text="Email")
                trv.heading("4", text="Phone_Number")
                trv.heading("5", text="Issue_Date")
                trv.heading("6", text="Name_of_Book_issued")
                trv.heading("7", text="Book_Number")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5],i[6]))
                trv_scroll = ttk.Scrollbar(f1, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set

                b1=tk.Button(win4,text="Click to Go Back",command=win4.destroy).place(x=550,y=350)

            def B5():

                win5 = Toplevel(root)
                win5.geometry("480x400+680+290")
                win5.resizable(False,False)
                win5.title("New Registration")
                win5.configure(bg="#B9F3FC")

                l2 = tk.Label(win5, text="New Registration", bg="#B9F3FC", font=('Arial', 15, 'bold')).place(x=145, y=10)

                f1 = tk.Frame(win5)
                f1.configure(bg="#B9F3FC")
                f1.pack(side="left", anchor="n", padx=30, pady=60)
                f2 = tk.Frame(win5)
                f2.configure(bg="#B9F3FC")
                f2.pack(side="left", anchor="n", padx=30, pady=60)
                f3 = tk.Frame(win5)

                def Register():
                    a_=a__.get()
                    b_=b__.get()
                    c_=c__.get()
                    d_=d__.get()
                    if a_!='' or len(a_)>4:
                        if len(b_)==10 :
                            if b_[0] in ['9','8','7','6','5']:
                                if c_!='' and c_[-10:]=="@gmail.com" or c_[-7:]==".edu.in":
                                    if len(d_)==12 or len(d_)==14 :
                                        def b22():
                                            a_a=f()
                                            sql1="insert into registration(ID,Name,Phone_No,Email,Aadhar) values(%s,%s,%s,%s,%s)"
                                            Values=[a_a,a_,b_,c_,d_]
                                            cur.execute(sql1,Values)
                                            mydb.commit()

                                            server = smtplib.SMTP('smtp.gmail.com', 587)
                                            server.starttls()
                                            server.login("librarymg0123@gmail.com", "ypswfhklylhurbvm")
                                            msg = 'Hello,Your Registration Id is ' + a_a +"\n Thank you for joining us"
                                            server.sendmail("librarymg0123@gmail.com", c_, msg)
                                            server.close()
                                            win22 = Toplevel(win5)
                                            win22.geometry("450x140+640+260")
                                            win22.title("BOOK RETURNED")
                                            win22.configure(bg="#B9F3FC")
                                            b2 = Button(win22, text="EXIT", width=13, height=2, bg="white",command=win22.destroy).place(x=170, y=75)
                                            l1 = Label(win22, text="  YOUR ARE REGISTERED  ", bg="#B9F3FC",font=("ARIAL 15 bold")).place(x=70, y=20)
                                            a__.set("")
                                            b__.set("")
                                            c__.set("")
                                            d__.set("")
                                            win24.destroy()
                                            mydb.commit()

                                        win24=Toplevel(win5)
                                        win24.geometry("480x160+640+260")
                                        win24.title("YOU ARE REGISTERED")
                                        win24.configure(bg="#B9F3FC")
                                        b2 = Button(win24, text="EXIT", width=13, height=2, bg="white",command=win24.destroy).place(x=255, y=95)
                                        b2 = Button(win24, text="SUBMIT", width=13, height=2, bg="white",command=b22).place(x=125, y=95)
                                        l1 = Label(win24,text="LIFETIME MEMBERSHIP AMOUNT IS 8000 \n AND FOR LATE RETURN 2Rs PER DAY",bg="#B9F3FC", font=("ARIAL 12 bold")).place(x=25, y=20)
                                    else:
                                        win2 = Toplevel(win5)
                                        l1 = tk.Label(win2, text="INCORRECT AADHAR").pack()
                                        b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                                else:
                                    win2 = Toplevel(win5)
                                    l1 = tk.Label(win2, text="INCORRECT EMAIL").pack()
                                    b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                            else:
                                win2 = Toplevel(win5)
                                l1 = tk.Label(win2, text="INCORRECT PHONE NUMBER").pack()
                                b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                        else:
                            win2 = Toplevel(win5)
                            l1 = tk.Label(win2, text="INCORRECT PHONE NUMBER").pack()
                            b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                    else:
                        z1 = Toplevel(win5)
                        l1 = tk.Label(z1, text="Please Enter your name").pack()
                        b1 = tk.Button(z1, text="Retry", bg="#AEE2FF", command= z1.destroy).pack(pady=10)

                b1 = tk.Button(win5, text="Register", width=10, command=Register).place(x=140, y=340)
                b5 = tk.Button(win5, text="Back", width=10, command=win5.destroy).place(x=270, y=340)
                # Message Box Missing
                a__ = tk.StringVar()
                b__ = tk.StringVar()
                c__ = tk.StringVar()
                d__ = tk.StringVar()

                l1 = tk.Label(f1, text="Enter Student Name", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l2 = tk.Label(f1, text="Enter your Phone_No", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l3 =  tk.Label(f1, text="Enter your Email ", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")
                l4 = tk.Label(f1, text="AAdhar", bg="#B9F3FC").pack(pady=20, side="top", anchor="w")

                E1 = tk.Entry(f2, textvariable=a__,width=30).pack(pady=20)
                E2 = tk.Entry(f2, textvariable=b__,width=30).pack(pady=20)
                E3 = tk.Entry(f2, textvariable=c__,width=30).pack(pady=20)
                E4 = tk.Entry(f2, textvariable=d__,width=30).pack(pady=20)

                #a_a is the random number generated

            def B6():
                win4 = Toplevel(root)
                cur.execute("select * from registration")
                b = cur.fetchall()
                win4.geometry("950x400+470+310")
                win4.resizable(False, False)
                win4.configure(bg="#B9F3FC")
                win4.title("REGISTERED MEMBERS")

                f1 = tk.Frame(win4, bg="#B9F3FC")
                f1.pack(pady=20, padx=10)

                trv = ttk.Treeview(f1, selectmode='browse', height=12)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2", "3", "4", "5")
                trv["show"] = 'headings'

                style = ttk.Style()
                # style.theme_use("clam")
                style.configure('Treeview',
                                background="#BFEAF5",
                                forecolor="black",
                                fieldcolor="#BFEAF5")
                style.configure('Treeview.Heading', backgound="green")
                style.map('Treeview',
                          background=[('selected', 'orange')])

                trv.column("1", width=140, anchor='c')
                trv.column("2", width=200, anchor='c')
                trv.column("3", width=120, anchor='c')
                trv.column("4", width=250, anchor='c')
                trv.column("5", width=140, anchor='c')
                trv.heading("1", text="Id")
                trv.heading("2", text="Name")
                trv.heading("3", text="Phone_Number")
                trv.heading("4", text="Email")
                trv.heading("5", text="Aadhar")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4]))
                trv_scroll = ttk.Scrollbar(f1, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set
                b1 = tk.Button(win4, text="Click to Go Back", command=win4.destroy).place(x=420, y=350)

            win3.configure(bg="#e697f7")

            try:
                from ctypes import windll
                windll.shcore.SetProcessDpiAwareness(1)
            except:
                pass

            lab = tk.Label(win3, bg="#e697f7", image=photo2)
            lab.place(x=80,y=180)
            l1 = Label(win3, text="THE OPTION WINDOW", bg="white", fg="red", font=("ARIAL", 40, "bold")).pack(side="top", fill="x")
            b1 = Button(win3,text="ISSUE A BOOK", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=B1).place(x=590, y=150)
            b2 = Button(win3,text="CHANGE BOOK STOCK", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=B2).place(x=940, y=150)
            b3 = Button(win3,text="RETURN BOOk", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=B3).place(x=590, y=290)
            b4 = Button(win3,text="VIEW BOOK ISSUED", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=B4).place(x=940, y=290)
            b5 = Button(win3,text="NEW REGISTRATION", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=B5).place(x=590, y=430)
            b6 = Button(win3,text="REGISTERED MEMBER", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=B6).place(x=940, y=430)
            b7 = Button(win3,text="EXIT", width=25, height=4, bg="white", font=("ARIAL", 10, "bold"),command=win3.destroy).place(x=770, y=570)
        else:
            win2=Toplevel(root)
            win2.geometry("280x120+840+370")
            l1=tk.Label(win2,text="INCORRECT PASSWORD",font="ARIAL 11 bold").pack(padx=20,pady=20)
            b1=tk.Button(win2,text="Retry",bg="#AEE2FF",width=10,command=win2.destroy).pack(pady=10)



    B3 = tk.Button(win1, text="SUBMIT",font=("ARIAL",10,"bold"),height=2, width=20,bg="white", command=B1)
    B3.place(x=75,y=300)
    E1.bind("<Return>",B1)


    B2 = tk.Button(win1, text="QUIT",font=("ARIAL",10,"bold"),height=2, width=20,bg="white",command=win1.destroy)
    B2.place(x=320,y=300)



# BUTTON MAIN WINDOW
b1 = tk.Button(f1, text="P-BOOKS", height=4, width=30, bg="#CE1212",fg="white",font=("Arial",10,"bold"), command=admin)
b1.pack(side="top", pady=10)

b2 = tk.Button(f1, text="Ebooks", height=4, width=30, bg="#CE1212",fg="white",font=("Arial",10,"bold"),command=BEbook)
b2.pack(side="left",pady=20)

root.mainloop()
