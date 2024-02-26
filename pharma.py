#https://youtu.be/DFHFSpo5dvI?t=541
from tkinter import *
from tkintermapview import TkinterMapView

root = Tk()
root.geometry('880x450')
root.title('pharmacies in duty')
root.iconbitmap('download (2).ico')
root.configure(background='lightgreen')

#-------title --------
title1 = Label(root,text='Pharmacies in duty project',
               fg='white',bg='black',
               font=('Tajawal',18))
title1.pack(fill=X)

#-------logo --------

logo = PhotoImage(file='gitcourse.txt/main/pngtree-pharmacy-snake-medical-bowl-png-image_6534987.png')
lab_logo = Label(root,image=logo,bd=0)
lab_logo.place(x=30,y=40)
#https://youtu.be/DFHFSpo5dvI?t=901

#-----label + entry + button -----
l = Label(root,text= 'country',font=('Tajawala',14),fg='black',bg='white')
l.place(x=40,y=410)

en = Entry(root,font=('Tajawala',14),width=10,bd=1,relief=GROOVE)
en.place(x=130,y=410)

b1 = Button(root,text='get country',bg='black',fg='white',
            bd=1,relief=SOLID,width=10,cursor='hand2')
b1.place(x=270,y=410)

b = Button(root,text='pharmacy central',bg='white',fg='black',bd=1,relief=SOLID,width=10,cursor='hand2',font=('Tajawal 13'))
b.place(x=40,y=450)
#https://youtu.be/DFHFSpo5dvI?t=1426


root.mainloop()