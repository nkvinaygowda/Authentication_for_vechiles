from tkinter import *
import time
import Access_Denied_Handler
import Access_Granted_Handler
from E_Mail_backend import *
from Access_Granted_Handler import *
import cv2

def close():
	time.sleep(1)
	win.destroy()

user_email = ''
name = ''
emails = []

def scan():
	global id, user_email , name , emails
	win.destroy()
	granted = Access_Granted_Handler.scan_code(id)
	if granted:
		user_email = user_mail(id)
		name = user_name(id)
		emails = all_emails()
		send_mail_to_all(emails ,user_email  , name ,'User Login Found' , 'Logged In')

id , closed = Access_Denied_Handler.main()

if ((id == '404') | closed):

	win2 = Tk()
	win2.geometry('400x300')
	win2.title('ERROR....!!!!')
	win2.config(bg='black')
	l1 = Label(win2, text='Face Not Detected' , width=30 , padx=3 , font = ('calibre',15), bg = 'black' , fg = 'red')
	l1.place(relx = 0.5, rely = 0.5 , anchor = 'center')
	win2.mainloop()

else:
	win = Tk()
	win.geometry('600x200')
	win.title('Verification Window')
	win.config(bg='Lightskyblue')

	l = Label(win, text='Show The QR Code You Have' , width=40 , padx=3 , font = ('calibre',15) , bg = 'lightgreen')
	l.place(x=80,y=50)
	b = Button(win, text='Open Camera' , font=('Ubuntu', 10) ,bg = 'red', command = scan)
	b.place(x = 230, y = 150)
	win.mainloop()





# win = Tk()
# win.geometry('600x600')
# win.title('Verification Window')
# win.config(bg='Lightskyblue')

# l = Label(win, text='Sending QR Code To The Registered Email' , width=40 , padx=3 , font = ('calibre',15) , bg = 'lightgreen')
# l.place(x=80,y=50)

# # sent = main.send_mail(id)

# # l1 = Label(win, text='Email Sent' , width=10 , padx=3 , font = ('calibre',15) , bg = 'blue')
# # l1.place(x=230,y=120)

# l1 = Label(win, text='Error....Email Not Sent ' , width=20 , padx=3 , font = ('calibre',15) , bg = 'black', fg = 'red')
# l1.place(x=170,y=120)

# # l2 = Label(win, text='Show The QR Code To The Camera' , width=30 , padx=3 , font = ('calibre',15) , bg = 'lightgreen')
# # l2.place(x=130,y=190)

# # b = Button(win, text='Open Camera' , font=('Ubuntu', 10) ,bg = 'red')
# # b.place(x = 230, y = 260)

# b = Button(win, text='Close' , font=('Ubuntu', 10) ,bg = 'red')
# b.place(x = 260, y = 190)


# win.mainloop()
