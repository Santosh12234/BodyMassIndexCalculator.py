from tkinter import *
root = Tk()
root.geometry("405x350")
root.title("BMI CALCULATOR")
root.config(bg="gray")
root.resizable(False,False)

def check():
    bmi = float((float(entry_1.get()))/(int((float(entry_2.get())/100)*(float(entry_2.get())/100))))
    if bmi>0:
        if bmi<=16:
            label_5.config(text="Your are severely underweight")
        elif bmi<=18.5:
            label_5.config(text="Your are underweight")
        elif bmi<=25:
            label_5.config(text="Your are Healthy")
        elif bmi<=30:
            label_5.config(text="Your are overweight")
        else:
            label_5.config(text="Your are severely overweight")
    else:
        label_5.config(text="")
    label_4.config(text=("Your BMI is "+str(bmi)))

label_1 = Label(root,width=27,bg="black",height=2,font=("candra",19),text="𝐁𝐌𝐈 𝐂𝐀𝐋𝐂𝐔𝐋𝐀𝐓𝐎𝐑",fg="white")
label_1.place(x=0,y=0)

label_2 = Label(root,width=32,bg="gray",height=1,font=("candra",18),text="𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐖𝐄𝐈𝐆𝐇𝐓 𝐈𝐍 𝐊𝐆:",fg="black")
label_2.place(x=-80,y=100)

label_3 = Label(root,width=32,bg="gray",height=1,font=("candra",18),text="𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐇𝐄𝐈𝐆𝐇𝐓 𝐈𝐍 𝐂𝐌 :",fg="black")
label_3.place(x=-80,y=145)

entry_1 = Entry(root,width=17,borderwidth=0)
entry_1.place(x=285,y=104,height=25)

entry_2 = Entry(root,width=17,borderwidth=0)
entry_2.place(x=285,y=150,height=25)

button_1 = Button(root,width=20,height=1,text="EXIT",bg="red",font=("candra",12),command=lambda:exit(0))
button_1.place(x=12,y=195)

button_2 = Button(root,width=19,height=1,text="CALCULATE",bg="green",font=("candra",12),command=lambda:check())
button_2.place(x=209,y=195)

label_4 = Label(root,width=41,bg="gray",height=1,font=("candra",13),fg="black")
label_4.place(x=12,y=250)

label_5 = Label(root,width=34,bg="gray",height=1,font=("candra",15),fg="black")
label_5.place(x=12,y=290)



root.mainloop()