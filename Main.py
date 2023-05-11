from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

#initializing the screen 
screen = Tk()
screen.geometry("600x400")
screen.title("My-Bank")
screen.configure(bg="light cyan")
screen.resizable("False","False")

#creating a database
connect = sqlite3.connect('bankdata.db')

#creating a cursor for keeping track on rows or column
cursor = connect.cursor()

#Creating the rows and columns
#cursor.execute("""
#    CREATE TABLE bankdata(
#        Name text,
#        Account_no integer,
#       ph_no integer,
#        age integer,
#        pin integer,
#        Balance integer
#    )
    
#""")


#Setting the title Background
titlbg = Label(screen,bg="DarkViolet",height=5)
titlbg.grid(row=0,column=0,ipadx=327,columnspan=4)

#setting the title 
title = Label(screen,text="My-",foreground="black",bg="DarkViolet",font=("Times New Roman",18),height=2)
title.grid(row=0,column=0,columnspan=2,padx=(250,0))
title2 = Label(screen,text="Bank",foreground="white",bg="DarkViolet",font=("Segoe Script",17),height=2)
title2.grid(row=0,column=2,padx=(0,290))

#setting the label name 
password = Label(screen,text="Account no",bg="light cyan",font=("Courier",15))
password.grid(row=1,column=0,columnspan=2,pady=(20,0))
Acno = Label(screen,text="Pin Number",bg="light cyan",font=("Courier",15))
Acno.grid(row=2,column=0,columnspan=2,pady=(20,0))

#setting up the entrys 
acEntry = Entry(screen,width=40)
acEntry.grid(row=1,column=1,columnspan=2,pady=(20,0))
pinEntry = Entry(screen,width=40,show="*")
pinEntry.grid(row=2,column=1,columnspan=2,pady=(20,0))

#setting the Login button

#setting the Create a A/c button

def register():
    nscreen = Toplevel()
    nscreen.geometry("600x470")
    nscreen.title("My-Bank Register")
    nscreen.configure(bg="light cyan")
    nscreen.resizable("False","False")

    #Setting the title Background
    titlbg = Label(nscreen,bg="DarkViolet",height=5)
    titlbg.grid(row=0,column=0,ipadx=327,columnspan=4)

    #setting the title 
    title = Label(nscreen,text="My-",foreground="black",bg="DarkViolet",font=("Times New Roman",18),height=2)
    title.grid(row=0,column=0,columnspan=2,padx=(250,0))
    title2 = Label(nscreen,text="Bank",foreground="white",bg="DarkViolet",font=("Segoe Script",17),height=2)
    title2.grid(row=0,column=2,padx=(0,290))


    #setting the label name 
    name = Label(nscreen,text="Name",bg="light cyan",font=("Courier",15))
    name.grid(row=1,column=0,columnspan=2,pady=(40,0))
    ac_no = Label(nscreen,text="Account No",bg="light cyan",font=("Courier",15))
    ac_no.grid(row=2,column=0,columnspan=2,pady=(20,0))
    phno = Label(nscreen,text="Phone no",bg="light cyan",font=("Courier",15))
    phno.grid(row=3,column=0,columnspan=2,pady=(20,0))
    Age = Label(nscreen,text="Age",bg="light cyan",font=("Courier",15))
    Age.grid(row=4,column=0,columnspan=2,pady=(20,0))
    pin = Label(nscreen,text="Pin Number",bg="light cyan",font=("Courier",15))
    pin.grid(row=5,column=0,columnspan=2,pady=(20,0))
    
    #setting up the entrys 
    Nameentry = Entry(nscreen,width=40)
    Nameentry.grid(row=1,column=1,columnspan=2,pady=(40,0))
    acentry = Entry(nscreen,width=40)
    acentry.grid(row=2,column=1,columnspan=2,pady=(20,0))
    phEntry = Entry(nscreen,width=40)
    phEntry.grid(row=3,column=1,columnspan=2,pady=(20,0))
    AgeEntry = Entry(nscreen,width=40)
    AgeEntry.grid(row=4,column=1,columnspan=2,pady=(20,0))
    pin_entry = Entry(nscreen,width=40)
    pin_entry.grid(row=5,column=1,columnspan=2,pady=(20,0))


    #Creating the save button
    def add():
        ac_true = FALSE
        age_true = FALSE
        if len(acentry.get())<6 and len(acentry.get())>8:
             messagebox.showerror("Ac_Limit","The Account no should be a minimum 6 no and maximum 8")
        else:
             ac_true = TRUE
        
        if int(AgeEntry.get())<=18:
             messagebox.showerror("Age_limit","The Minimum Age to create a Account is 18")
        else:
             age_true = TRUE


        if ac_true == TRUE and age_true == TRUE:
             
            #creating a database
            connect = sqlite3.connect('bankdata.db')

            #creating a cursor for keeping track on rows or column
            cursor = connect.cursor()

            #Execute
            cursor.execute("INSERT INTO bankdata VALUES(:Name,:acno,:phno,:age,:pin,:balance)",
            {
                "Name":Nameentry.get(),
                "acno":acentry.get(),
                "phno":phEntry.get(),
                "age":AgeEntry.get(),
                "pin":pin_entry.get(),
                "balance":000
            })
            #commiting the changes done 
            connect.commit()
            #closing the database
            connect.close()

            #Deleting the text from entry boxes 
            Nameentry.delete(0,END)
            acentry.delete(0,END)
            phEntry.delete(0,END)
            AgeEntry.delete(0,END)
            pin_entry.delete(0,END)

    save = Button(nscreen,text="Save",bg="Blue Violet",foreground="black",font=('Fixedys',14,"bold"),command=add)
    save.grid(row=7,column=0,columnspan=3,ipadx=20,pady=(40,0),padx=(0,30))

NewAc = Button(screen,text="Create a new A/c",bg="dark sea green",foreground="black",font=('Fixedys',14,"bold"),command=register)
NewAc.grid(row=5,column=0,columnspan=3,ipadx=20,pady=(30,0),padx=(0,30))

def login():
    
        if acEntry.get() =="" or pinEntry.get() =="":
            messagebox.showerror("Error","Please enter all the fields!")


        #creating a show menu only for admin 
        elif acEntry.get()=="admin" and pinEntry.get() == "1234":
            
            newscreen = Toplevel()
            newscreen.title("Student Data")
            newscreen.geometry("700x600")
            newscreen.config(bg="black")
            newscreen.resizable("False","False")

            tree = ttk.Treeview(newscreen,selectmode="browse",height=25)
            tree.grid(row=0,column=0,columnspan=4)
            style = ttk.Style(newscreen)
            style.theme_use('clam')
            style.configure("Treeview",background="black",fieldbackground="black",foreground="white")


            tree["columns"] = ("1","2","3","4","5","6","7")
            tree["show"] = "headings"


            tree.column("1",anchor="center",width=60)
            tree.heading("1", text="ID")

            tree.column("2",anchor="center",width=120)
            tree.heading("2",text="Name")

            tree.column("3",anchor="center",width=110)
            tree.heading("3",text="Account Number")

            tree.column("4",anchor="center",width=116)
            tree.heading("4",text="Phone Number")
            
            tree.column("5",anchor="center",width=70)
            tree.heading("5",text="Age")
            
            tree.column("6",anchor="center",width=110)
            tree.heading("6",text="Pin Number")

            tree.column("7",anchor="center",width=110)
            tree.heading("7",text="Balance")
        
        
            #creating a database
            connect = sqlite3.connect('bankdata.db')
            #creating a cursor for keeping track on rows or column
            cursor = connect.cursor()

            # Adding the values                            
            cursor.execute('SELECT oid,* FROM bankdata')
            records = cursor.fetchall()
            for row in records:
                tree.insert("",'end',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

            #commiting the changes done 
            connect.commit()
            #closing the database
            connect.close()

            #deleting a row 
            def deletes():
                #creating a database
                connect = sqlite3.connect('bankdata.db')
                #creating a cursor for keeping track on rows or column
                cursor = connect.cursor()
                selected = tree.selection()[0]
                id = ""
                if selected[2] != "0":
                    id = selected[2:4]
                else:
                    id = selected[3]
                tree.delete(selected)

                # Adding the values                            
                cursor.execute("DELETE from bankdata WHERE oid="+id)
                
                
                #commiting the changes done 
                connect.commit()
                #closing the database
                connect.close()

            dell = Button(newscreen,text="Remove Account",command=deletes,activebackground="red")
            dell.grid(row=1,column=0,columnspan=2,ipadx=40,ipady=10,pady=(10,0))

            def update():
                editor = Toplevel()
                editor.title("Update")
                editor.geometry("670x470")
                editor.resizable("False","False")
                editor.config(bg="light cyan")

                #Setting the title Background
                titlbg = Label(editor,bg="DarkViolet",height=5)
                titlbg.grid(row=0,column=0,ipadx=327,columnspan=4)

                #setting the title 
                title = Label(editor,text="My-",foreground="black",bg="DarkViolet",font=("Times New Roman",18),height=2)
                title.grid(row=0,column=0,columnspan=2,padx=(250,0))
                title2 = Label(editor,text="Bank",foreground="white",bg="DarkViolet",font=("Segoe Script",17),height=2)
                title2.grid(row=0,column=2,padx=(0,290))


                #setting the label name 
                name = Label(editor,text="Name",bg="light cyan",font=("Courier",15))
                name.grid(row=1,column=0,columnspan=2,pady=(40,0))
                ac_no = Label(editor,text="Account No",bg="light cyan",font=("Courier",15))
                ac_no.grid(row=2,column=0,columnspan=2,pady=(20,0))
                phno = Label(editor,text="Phone no",bg="light cyan",font=("Courier",15))
                phno.grid(row=3,column=0,columnspan=2,pady=(20,0))
                Age = Label(editor,text="Age",bg="light cyan",font=("Courier",15))
                Age.grid(row=4,column=0,columnspan=2,pady=(20,0))
                pin = Label(editor,text="Pin Number",bg="light cyan",font=("Courier",15))
                pin.grid(row=5,column=0,columnspan=2,pady=(20,0))
                
                #setting up the entrys 
                Nameentry2 = Entry(editor,width=40)
                Nameentry2.grid(row=1,column=1,columnspan=2,pady=(40,0))
                acentry2 = Entry(editor,width=40)
                acentry2.grid(row=2,column=1,columnspan=2,pady=(20,0))
                phEntry2 = Entry(editor,width=40)
                phEntry2.grid(row=3,column=1,columnspan=2,pady=(20,0))
                AgeEntry2 = Entry(editor,width=40)
                AgeEntry2.grid(row=4,column=1,columnspan=2,pady=(20,0))
                pin_entry2 = Entry(editor,width=40)
                pin_entry2.grid(row=5,column=1,columnspan=2,pady=(20,0))

                #converting the id into single value
                selected = tree.selection()[0]
                id = ""
                if selected[2] != "0":
                    id = selected[2:4]
                else:
                    id = selected[3]

                #creating a database
                connect = sqlite3.connect('bankdata.db')
                #creating a cursor for keeping track on rows or column
                cursor = connect.cursor()

                # Adding the values                            
                cursor.execute('SELECT * FROM bankdata WHERE oid='+id)
                records = cursor.fetchall()      
                
                for row in records:
                    Nameentry2.insert(0,row[0])
                    acentry2.insert(0,row[1])
                    phEntry2.insert(0,row[2])
                    AgeEntry2.insert(0,row[3])
                    pin_entry2.insert(0,row[4])


                #Updating sql Command
                def updat():
                    #creating a database
                    connect = sqlite3.connect('bankdata.db')
                    #creating a cursor for keeping track on rows or column
                    cursor = connect.cursor()

                    # updating the values                            
                    cursor.execute('''UPDATE bankdata SET
                    Name=:naam,
                    Account_no=:acno,
                    ph_no=:pno,
                    age=:age,
                    pin=:pin
                    WHERE oid = :oid''',
                    {
                        "oid":id,
                        "naam":Nameentry2.get(),
                        "acno":acentry2.get(),
                        "pno":phEntry2.get(),
                        "age":AgeEntry2.get(),
                        "pin":pin_entry2.get()
                    })
                    
                    records = cursor.fetchall()      
                    #commiting the changes done 
                    connect.commit()
                    #closing the database
                    connect.close()

                    Nameentry2.delete(0,END)
                    acentry2.delete(0,END)
                    phEntry2.delete(0,END)
                    AgeEntry2.delete(0,END)
                    pin_entry2.delete(0,END)


                
                upd = Button(editor,text="Update",command=updat,bg="DarkViolet")
                upd.grid(row=6,column=0,columnspan=4,ipadx=30,ipady=10,pady=(14,0))

            upt = Button(newscreen,text="Update Data",command=update,activebackground="gold")
            upt.grid(row=1,column=2,columnspan=2,ipadx=40,ipady=10,pady=(10,0))

        else:
            
            #creating a database
            connect = sqlite3.connect('bankdata.db')

            #creating a cursor for keeping track on rows or column
            cursor = connect.cursor()

            #execute
            cursor.execute("SELECT oid,Name,Account_no,Balance,pin FROM bankdata WHERE Account_no="+str(acEntry.get()))
            values = cursor.fetchall()
            for row in values:

                if str(row[2])==acEntry.get() and str(row[4])==pinEntry.get():
                    logscreen = Toplevel()
                    logscreen.geometry("600x400")
                    logscreen.title("My-Bank Login")
                    logscreen.configure(bg="light cyan")
                    logscreen.resizable("False","False")

                    #Setting the title Background
                    titlbg = Label(logscreen,bg="DarkViolet",height=5)
                    titlbg.grid(row=0,column=0,ipadx=400,columnspan=4)

                    #setting the title 
                    title = Label(logscreen,text="My-",foreground="black",bg="DarkViolet",font=("Times New Roman",18),height=2)
                    title.grid(row=0,column=0,columnspan=2,padx=(250,0))
                    title2 = Label(logscreen,text="Bank",foreground="white",bg="DarkViolet",font=("Segoe Script",17),height=2)
                    title2.grid(row=0,column=2,padx=(0,410))

                    #Setting the values 
                    name = Label(logscreen,text="Name",bg="light cyan",font=("Courier",15))
                    name.grid(row=1,column=0,columnspan=2,pady=(40,0))
                    ac_no = Label(logscreen,text="Account No",bg="light cyan",font=("Courier",15))
                    ac_no.grid(row=2,column=0,columnspan=2,pady=(20,0))
                    Balance = Label(logscreen,text="Balance",bg="light cyan",font=("Courier",15))
                    Balance.grid(row=3,column=0,columnspan=2,pady=(20,0))


                    name = Label(logscreen,text=row[1],bg="light cyan",font=("Courier",15))
                    name.grid(row=1,column=1,columnspan=2,pady=(40,0),padx=(0,80))
                    ac_no = Label(logscreen,text=row[2],bg="light cyan",font=("Courier",15))
                    ac_no.grid(row=2,column=1,columnspan=2,pady=(20,0),padx=(0,80))
                    Bal_no = Label(logscreen,text=row[3],bg="light cyan",font=("Courier",15))
                    Bal_no.grid(row=3,column=1,columnspan=2,pady=(20,0),padx=(0,80))

                    id = row[0]

                    #Deposit box
                    def deposit():
                        #Connecting the database
                        connect = sqlite3.connect('bankdata.db')

                        #creating a cursor for keeping track on rows or column
                        cursor = connect.cursor()

                        cursor.execute("SELECT Balance FROM bankdata WHERE oid="+str(id))
                        prvbal = cursor.fetchone()

                        nBal = int(prvbal[0])+int(dep_entry.get())

                        #execute
                        cursor.execute("""UPDATE bankdata SET 
                        Balance=:depbal
                        WHERE oid=:oid""",{
                             "depbal":nBal,
                             "oid":id
                        })

                        #commiting the changes done 
                        connect.commit() 
                        #closing the database
                        connect.close()
                        
                        dep_entry.delete(0,END)


                    dep_entry = Entry(logscreen,width=20)
                    dep_entry.grid(row=4,column=0,pady=(30,0),padx=(50,0))
                    dep = Button(logscreen,text="Deposit",bg="Blue Violet",foreground="black",font=('Fixedys',14,"bold"),command=deposit)
                    dep.grid(row=5,column=0,pady=(30,0),padx=(50,0))

                    #Widthraw Box
                    def Widthraw():
                        #Connecting the database
                        connect = sqlite3.connect('bankdata.db')

                        #creating a cursor for keeping track on rows or column
                        cursor = connect.cursor()

                        #execute
                        cursor.execute("SELECT Balance FROM bankdata WHERE oid="+str(id))
                        balances = cursor.fetchone()

                        newBal = int(balances[0])-int(wid_entry.get())
                        if newBal<0:
                             messagebox.showerror("Insuffient Funds","You Have Insuffient Funds")
                        else:
                            cursor.execute("""UPDATE bankdata SET 
                            Balance=:bal
                            WHERE oid=:oid""",{
                                "bal":newBal,
                                "oid":id
                            })


                        #commiting the changes done 
                        connect.commit() 
                        #closing the database
                        connect.close()

                        wid_entry.delete(0,END)

                    wid_entry = Entry(logscreen,width=20)
                    wid_entry.grid(row=4,column=1,columnspan=2,pady=(30,0),padx=(0,80))
                    wid = Button(logscreen,text="Widthraw",bg="Blue Violet",foreground="black",font=('Fixedys',14,"bold"),command=Widthraw)
                    wid.grid(row=5,column=1,columnspan=2,pady=(30,0),padx=(0,80))


                elif str(row[2])!=acEntry.get():
                    messagebox.showerror("No account!","No account exist")
                elif str(row[4])!=pinEntry.get():
                    messagebox.showerror("Pin Error","Wrong Pin")

            #commiting the changes done 
            connect.commit() 
            #closing the database
            connect.close()

log = Button(screen,text="Login",bg="Blue Violet",foreground="black",font=('Fixedys',14,"bold"),command=login)
log.grid(row=4,column=0,columnspan=3,ipadx=20,pady=(40,0),padx=(0,30))

#commiting the changes done 
connect.commit()
#closing the database
connect.close()

screen.mainloop()