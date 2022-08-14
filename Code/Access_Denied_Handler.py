from tkinter import *
from tkinter import messagebox
import time
from Access_Granted_Handler import *
from E_Mail_backend import *

win1 = Tk()
id = ''

def win_2():
	win2 = Tk()
	win2.geometry('400x300')
	win2.title('ERROR....!!!!')
	win2.config(bg='black')
	l1 = Label(win2, text='ACCESS DENIED....!!!' , width=30 , padx=3 , font = ('calibre',15), bg = 'black' , fg = 'red')
	l1.place(relx = 0.5, rely = 0.5 , anchor = 'center')
	win2.mainloop()

closed = False

def on_closing():
	global closed
	if (messagebox.askokcancel("Quit", "Do you want to quit?")):
		closed = True
		win1.destroy()
		return closed

def capture_and_send_mail(emails):
	cam = cv2.VideoCapture(0)
	result, image = cam.read()
	cv2.imwrite('unknown_user.png' , image)
	if result:
		filename = f'unknown_user.png'
		send_mail_to_all(emails , None , 'Unknown Person',  'Action Required!!!',  'Tried To Login' , filename = filename)
	else:
		send_mail_to_all(emails , None , 'Unknown Person',  'Action Required!!!',  'Tried To Login' ,  filename = None)


def open_cam():
	global id
	time.sleep(3)
	id = recog()
	name = user_name(id)
	if (id == '404'):
		emails = all_emails()
		capture_and_send_mail(emails)
		time.sleep(1)
		win1.destroy()
		# win_2()
	else:
		time.sleep(1)
		win1.destroy()

def main():
	global id , closed
	win1.geometry('350x200')
	win1.title('Detection Window')
	win1.config(bg='Lightskyblue')

	l = Label(win1, text='Click Open Camera \n Wait For The Camera To Open \n Look Into The Camera' , width=30 , padx=3 , font = ('calibre',15) , bg = 'lightgreen')
	l.place(x=5,y=30)
	win1.protocol("WM_DELETE_WINDOW", on_closing)

	b1 = Button(win1, text='Open Camera' , font=('Ubuntu', 10) ,bg = 'red',  command = open_cam)
	

	
	# b1 = Button(win1, text='Open Camera' , font=('Ubuntu', 10) , bg = 'red')
	b1.place(x = 120, y = 140)

	win1.mainloop()
	return id , closed




























