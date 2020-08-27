
import sys
from tkinter import *


root= Tk()
root.title('Product Name/Code Generator')
root.geometry("500x500")



#Naming section
pdname= Entry(root, text="ProductName",width=35)
pdcode=Entry(root, text="ProductCode",width=35)
#pdname.upper()

#Packing section
pdname.pack()
pdcode.pack()

#insert section
pdname.insert(1,"Enter Product Name")
pdcode.insert(0,"Enter Product Code")

def getinfo():
    i1=pdname.get()
    i2=pdcode.get()
    #d1=drop.get()
    l1=Label(root, text=i1)
    l2=Label(root, text=i2)
    l1.pack()
    l2.pack()


#Dropdown menu
clicked = StringVar()
drop=OptionMenu(root, clicked, "option1", "option2" )
clicked.set("        ")
drop.pack()


  

mybutton= Button(root, text="Submit", command=getinfo)
mybutton.pack()

Label(text="Product Lst").pack()
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)




root.mainloop()