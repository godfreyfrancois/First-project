import sys
from tkinter import *


root= Tk()
root.title('Product Name/Code Generator')
root.geometry("300x300")

#SQL data base connection


#Naming section
pdname= Entry(root, text="ProductName",width=30)
pdcode=Entry(root, text="ProductCode",width=30)
#pdname.upper()

#Text section
pdname.grid(row =0, column=1)
pdcode.grid(row =1, column=1)
#pdname.insert(0,"Enter Product Name")
#pdcode.insert(0,"Enter Product Code")

#Label Section
pdname_label=Label(root, text="Product Name:")
pdcode_label=Label(root, text="Product Code:")
pdname_label.grid(row=0, column=0)
pdcode_label.grid(row=1, column=0)

def getinfo():
    i1=pdname.get()
    i2=pdcode.get()
    #d1=drop.get()
    l1=Label(root, text=i1)
    l2=Label(root, text=i2)
    l1.grid()
    l2.grid()


def query():
	#db connection
	#connection=sqlite3.connect('productlist')
	
	#create cursor
	#c=conn.curseor()

	#select
	"""
	c.execute("SELECT * , oid dbname")
	r= c.fetchall()
	print (r)
	
	#loop
	print_records = ""
	for r in records:
		print_records += str(r) + "\n"

	query_label = label(root, text=print_records)
	query_label.grid()


			
   """

	#commitchanges
	#conn.commi()

	#close connection
	#conn.close()


def Submit():
	#db connection
	#connection=sqlite3.connect('productlist')
	
	#create cursor
	#c=conn.curseor()

	#insert into table
	"""
	c.execute("INSERT INTO table VALUES (:pdname, :pdcode")
			{
				'pdname': pdnmae.get(),
				'pdcode': pdcode.get()

			})

   """

	#commitchanges
	#conn.commi()

	#close connection
	#conn.close()

	#Clear entry
	pdname.delete(0, END)
	pdcode.delete(0, END)



#create query
querybtn=Button(root, test="Show records", command=query)
querybtn.grid()


#Submit Button
mybutton= Button(root, text="Submit" columnspan=2, command=Submit)
mybutton.grid()
#mybutton.place(relx=1.0, rely=1.0, anchor=CENTER)

"""
Label(text="Product Lst").grid()
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.grid(fill=X, padx=5, pady=5)
"""













# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))
root.mainloop()