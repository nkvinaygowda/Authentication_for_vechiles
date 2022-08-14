import Recognition_Backend as rt
import numpy as np
import pickle
import qrcode
import smtplib
import imghdr
from email.message import EmailMessage
import cv2
import random as  rd
import sys
from tkinter import *

sent =False
data_orig = 0


def all_emails():
    emails = []
    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()
    for key , value in ref_dictt.items():
        try:
            email = ref_dictt[key]['email']
            emails.append(email)
        except:
            pass

    return emails

def recog():
    name = rt.reco()
    return name

def user_name(name):
    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()
    return ref_dictt[name]['name']

def user_mail(name):
    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()
    return ref_dictt[name]['email']

def send_mail(name):
    global sent,  data_orig
    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()

    f=open("ref_embed.pkl","rb")
    embed_dictt=pickle.load(f)      #embed_dict- ref  vs embedding 
    f.close()

    data_orig = str(rd.randint(10000000 , 100000000))

    # data_orig = ref_dictt[name]['name']
    # output file name
    filename = "site.png"
    # generate qr code
    img = qrcode.make(data_orig)
    # save img to a file
    img.save(filename)

    # if(name == '404'):
    #     sys.exit("Access denied!!!")

    Sender_Email = "testfor2factor@gmail.com"
    Reciever_Email = ref_dictt[str(name)]['email']     
    Password = "cdnhgnzxbtoftchy"
    print("Hello ",ref_dictt[str(name)]['name'], " check your email and verify QR code.")

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "QR code for two-step verification" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Please verify by showing this QR code to camera.') 

    try:
        with open(filename, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name


        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename='verificaton code')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)

        print("MAIL SENT")
        sent =True

    except:
        sent = False

    return sent

Granted = False

def scan_code(id):
    global Granted
    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()
    name = ref_dictt[id]['name']
    filename = f'user_{name}.png'

    img = cv2.imread(filename)

    detector = cv2.QRCodeDetector()

    data_orig , bbox , strainght_qrcode = detector.detectAndDecode(img)

    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    count = 0
    while True:
        _, img = cap.read()
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image    
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                cv2.line(img, np.array(bbox[i][0]).astype(int), np.array(bbox[(i+1) % len(bbox)][0]).astype(int), color=(255, 0, 0), thickness=2)

            if data:
                print("[+] QR Code detected, data:", data)
                count += 1

        # display the result
        cv2.imshow("img", img)
        if (data == data_orig):
            cap.release()
            cv2.destroyAllWindows()
            win2 = Tk()
            win2.geometry('400x300')
            win2.title('SUCCESSFUL')
            win2.config(bg='black')
            l1 = Label(win2, text='ACCESS GRANTED...!!!' , width=30 , padx=3 , font = ('calibre',15), bg = 'black' , fg = 'red')
            l1.place(relx = 0.5, rely = 0.5 , anchor = 'center')
            win2.mainloop()
            print("ACCESS GRANTED")
            cv2.waitKey(delay = 5000)
            Granted = True
            break
        if (count == 5):
            cap.release()
            cv2.destroyAllWindows()
            win2 = Tk()
            win2.geometry('400x300')
            win2.title('ERROR....!!!!')
            win2.config(bg='black')
            l1 = Label(win2, text='ACCESS DENIED...!!!\nWRONG CODE SHOWN' , width=40 , padx=3 , font = ('calibre',15), bg = 'black' , fg = 'red')
            l1.place(relx = 0.5, rely = 0.5 , anchor = 'center')
            win2.mainloop()
            print("ACCESS DENIED")
            cv2.waitKey(delay = 5000)
            break
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return Granted

