import qrcode
import imghdr
import smtplib
from email.message import EmailMessage
import random as  rd


sent = True

def send_mail_to_all(emails , user_email , name ,subject, body, filename = None):
	Reciever_Email = emails
	Sender_Email = "testfor2factor@gmail.com"
	Password = "cdnhgnzxbtoftchy"
	newMessage = EmailMessage()
	newMessage['From'] = Sender_Email
	newMessage['To'] = Reciever_Email 
	newMessage['Subject'] = subject
	newMessage.set_content(f'{name} {body}')
	if filename:
		try:
			with open(filename, 'rb') as f:
				image_data = f.read()
				image_type = imghdr.what(f.name)
				image_name = f.name

			newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename='Unknown Person')


			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				smtp.login(Sender_Email, Password)
				smtp.send_message(newMessage)
				print("MAIL SENT TO USER")
		except:
			print("MAIL NOT SENT")

	else:
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(Sender_Email, Password)
			smtp.send_message(newMessage)
			print("Mail Sent To All Others")
		if (body == 'Successfully Registered'):
			subject = 'Registeration Successful'
			send_mail_to_one(name , subject , user_email)
		else:
			if user_email:
				subject = subject
				send_mail_to_one(name ,subject ,user_email)
			else:
				pass


def send_mail_to_one(name,subject, email):
	global sent
	Sender_Email = "testfor2factor@gmail.com"
	Reciever_Email = email
	Password = "cdnhgnzxbtoftchy"
	newMessage = EmailMessage()
	newMessage['Subject'] = subject

	newMessage['From'] = Sender_Email
	newMessage['To'] = Reciever_Email
	newMessage.set_content('Please Use This QR Code During Verification')
	data_orig = str(rd.randint(10000000 , 100000000))
	filename = f'user_{name}.png'
	img = qrcode.make(data_orig)
	img.save(filename)
	try:
		with open(filename, 'rb') as f:
			image_data = f.read()
			image_type = imghdr.what(f.name)
			image_name = f.name

		newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename='Verificaton Code')


		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(Sender_Email, Password)
			smtp.send_message(newMessage)

		print("MAIL SENT TO USER")
		sent =True

	except:
		sent = False


