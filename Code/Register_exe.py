from tkinter import *
import Register_backend as lud
import time
from E_Mail_backend import *

win = Tk()

win.geometry('600x600')
win.title('Registeration Window')
win.config(bg='Lightskyblue')

emails = []

def store_data():
	global emails
	ref_id = textin_id.get()
	name = textin_name.get()
	email = textin_email.get()
	ref_dictt, embed_dict , Data= lud.reg(ref_id , name , email)
	if Data:
		for key , value in ref_dictt.items():
			try:
				email = ref_dictt[key]['email']
				emails.append(email)
			except:
				pass
		user_id = f'ID:- {ref_id}'
		user_name = f'Name:- {name}'
		user_email = f'Email:- {email}'
		list.insert(0,user_id)
		list.insert(1,user_name)
		list.insert(2,user_email)
		emails.remove(email)
		send_mail_to_all(emails ,email  , name , 'Registeration Update', 'Successfully Registered')
	else:
		win.destroy()
		time.sleep(2)
		win2 = Tk()
		win2.geometry('400x300')
		win2.title('ERROR....!!!!')
		win2.config(bg='black')
		l1 = Label(win2, text='NO DATA STORED' , width=30 , padx=3 , font = ('calibre',15), bg = 'black' , fg = 'red')
		l1.place(relx = 0.5, rely = 0.5 , anchor = 'center')
		win2.mainloop()
		send_mail_to_all(emails,email ,name ,"Regsiteration Update" ,  'Failed To Register')

l = Label(win, text='USER REGISTRATION' , width=20 , padx=3 , font = ('calibre',15) , bg = 'lightgreen')
l.place(x=210,y=30)

l1 = Label(win, text='Enter ID' , font = ('calibre',10), bg = 'red', padx=3)
l1.place(x=285,y=100)
textin_id = StringVar()
e1 = Entry(win, width=30 , textvariable = textin_id,font=('Ubuntu', 15))
e1.place(x = 150 , y = 130)

l2 = Label(win, text='Enter Name' , font = ('calibre',10), bg = 'red', padx=3)
l2.place(x=280,y=170)
textin_name = StringVar()
e2 = Entry(win, width=30 , textvariable = textin_name,font=('Ubuntu', 15))
e2.place(x = 150 , y = 200)

l3 = Label(win, text='Enter Email' , font = ('calibre',10), bg = 'red', padx=3)
l3.place(x=280,y=240)
textin_email = StringVar()
e3 = Entry(win, width=30 , textvariable = textin_email,font=('Ubuntu', 15))
e3.place(x = 150 , y = 270)

b1 = Button(win, text='Register Myself' , font=('Ubuntu', 10) , command = store_data)
b1.place(x = 270 , y = 320)

l4 = Label(win, text='After Registering Wait For The Camera To Open \n Press "S" 5 Times To Capture Your Photo' , font = ('bold',10), bg = 'lightpink', padx=3)
l4.place(x=170,y=370)

l4 = Label(win, text='Registered User Info' , font = ('calibre',10), bg = 'red', padx=3)
l4.place(x=255,y=460)

list = Listbox(win, width=60 , height=5)
list.place(x=140,y=500)

win.mainloop()
