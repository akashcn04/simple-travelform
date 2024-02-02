from tkinter import *
root=Tk()
root.title("FORM")
root.geometry("444x444")
def getvals():
    print("submitting form")
    print(f"{namevalue.get(),phonevalue.get(),agevalue.get(),payvalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),agevalue.get(),payvalue.get()}")
#heading of form
Label(root,text="WELCOME TO BC TRAVELS",font="comicsonsms 15 bold").grid(row=0,column=3)
#what to fill? 
name=Label(root,text="Name",font='crimsonsms 9')
phone=Label(root,text="Phone_Number",font='crimsonsms 9 ')
sex=Label(root,text="Gender",font='crimsonsms 9')
pay=Label(root,text="Payment_Mode",font='crimsonsms 9')
#packed labels using grid
name.grid(row=1,column=2)
phone.grid(row=3,column=2)
sex.grid(row=5,column=2)
pay.grid(row=7,column=2)
#created tkinter Variable
namevalue=StringVar()
phonevalue=StringVar()
agevalue=StringVar()
payvalue=StringVar()
#entry of user
Entry(root,textvariable=namevalue).grid(row=1,column=3)
Entry(root,textvariable=phonevalue).grid(row=3,column=3)
Entry(root,textvariable=agevalue).grid(row=5,column=3)
Entry(root,textvariable=payvalue).grid(row=7,column=3)
#checkbox
Checkbutton(text="DO YOU ACCEPT ALL OUR RULES AND REGULATIONS?").grid(row=8,column=3)
#button
Button(text="SUBMIT",borderwidth=6,relief=GROOVE,command=getvals).grid(row=9,column=3)
root.mainloop()