import sys
import cv2 
import face_recognition
import pickle

def reg(ref_id, name , email):
    Exit = False
    Data = True
    try:
        f=open("ref_name.pkl","rb")
        ref_dictt=pickle.load(f)
        f.close()
    except:
        ref_dictt={}
    ref_dictt[ref_id] = dict()
    ref_dictt[ref_id]['name'] = name
    ref_dictt[ref_id]['email'] = email

    f=open("ref_name.pkl","wb")
    pickle.dump(ref_dictt,f)
    f.close()
    # try:
    embed_dictt={}
    f=open("ref_embed.pkl","rb")
    embed_dictt=pickle.load(f)
    f.close()
    # except:
    	

    for i in range(5):
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:       
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            
            key = cv2.waitKey(1)

            if key == ord('s') : 
                face_locations = face_recognition.face_locations(rgb_small_frame)
                if face_locations != []:
                    face_encoding = face_recognition.face_encodings(frame)[0]
                    if ref_id in embed_dictt:
                        embed_dictt[ref_id]+=[face_encoding]
                    else:
                        embed_dictt[ref_id]=[face_encoding]
                    webcam.release()
                    cv2.waitKey(1)
                    cv2.destroyAllWindows()     
                    break
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                Exit = True
                break

        if Exit:
            break

    f=open("ref_embed.pkl","wb")
    pickle.dump(embed_dictt,f)
    f.close()

    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()

    f=open("ref_embed.pkl","rb")
    embed_dictt=pickle.load(f)      #embed_dict- ref  vs embedding 
    f.close()

    return ref_dictt , embed_dictt , Data


