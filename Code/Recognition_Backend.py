import face_recognition
import cv2
import numpy as np
import glob
import time
import csv
import pickle
import statistics as st

def reco():
    f=open("ref_name.pkl","rb")
    ref_dictt=pickle.load(f)         #ref_dict=ref vs name
    f.close()

    f=open("ref_embed.pkl","rb")
    embed_dictt=pickle.load(f)      #embed_dict- ref  vs embedding 
    f.close()

    known_face_encodings = []  #encodingd of faces
    known_face_names = []      #ref_id of faces

    for ref_id , embed_list in embed_dictt.items():
        for embed in embed_list:
            known_face_encodings +=[embed]
            known_face_names += [ref_id]

    video_capture = cv2.VideoCapture(0)
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    Exit = False
    # global face_locations, face_names , face_encodings , process_this_frame , Exit
    ref_dictt['404'] = dict({'name':'Unknown'})
    f=open("ref_name.pkl","wb")
    pickle.dump(ref_dictt,f)
    f.close()
    # print(ref_dictt)
    while True  :
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            # print('locations: ' , face_locations)
            # if (face_locations):
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                # print("face_encoding" , face_encoding)
                # print(np.array(face_encoding).shape)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding , tolerance = 0.60)
                # print("matches: " , matches)
                if (matches):
                # name = "Unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    # print("dist: " , face_distances)
                    for i, face_distance in enumerate(face_distances):
                        if any(face_distances < 0.5):
                            # print("<0.5")
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name = known_face_names[best_match_index]
                                # print(name)
                            if ref_dictt[name] in list(ref_dictt.values()):
                                # print("Matched")
                                Exit = True
                            face_names.append(name)
                        else:
                            # print(">0.5")
                            face_names.append('404')
                            Exit = True
                else:
                    cv2.waitKey(delay = 5000)
                    face_names.append('404')
                    # print("NO DATA FOUND")
                    Exit = True
            # else:
            #     cv2.waitKey(delay = 5000)
            #     # name = '404'
            #     face_names.append('404')
            #     # print("NO DATA FOUND")
            #     Exit = True
        process_this_frame = not process_this_frame
        # print(face_names)
        for (top_s, right, bottom, left), name in zip(face_locations, face_names):
            try:
                top_s *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, ref_dictt[name]['name'], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            except:
                # print("Not Matched")
                pass
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if Exit:
            cv2.waitKey(delay = 3000)
            break
    video_capture.release()
    cv2.destroyAllWindows()
    if face_names:
        return st.mode(face_names)
