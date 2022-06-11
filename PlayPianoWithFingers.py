import cv2 as cv
import numpy as np
import time
import math
import HandTrackingModule as htm
# Defining camera size
wCam , hCam = 720,720

# Defining chords sizes
C =[[50,100],[100,200]]
Cd=[[100,100],[125,125]]
D =[[125,100],[175,200]]
E =[[200,100],[250,200]]
F =[[275,100],[325,200]]
G =[[350,100],[400,200]]
A =[[425,100],[475,200]]
B =[[500,100],[550,200]]
chordsList = [C,Cd,D,E,F,G,A,B]
chords = ['C','C#','D','E','F','G','A','B']

# Defining camera
vid = cv.VideoCapture(0)
vid.set(3,wCam)
vid.set(4,hCam)

# Hand detection
detector = htm.handDetector(min_detection_confidence=0.8)

def chordAreaControl():
    index = 0
    for chord in chordsList:
        if centerX <= chord[1][0]:
            if chord[0][0] <= centerX:
                if centerY <= chord[1][1]:
                    if chord[0][1] <= centerY:
                        # print(('C',centerX,centerY,(C[0][0],C[1][0]),(C[0][1],C[1][1])))
                        print(chords[index])
        index = index + 1

while True:
    success , img = vid.read()
    img = cv.flip(img,1)

    # Find hands
    img = detector.findHands(img,draw=False)

    # Creating piano chords
    cv.rectangle(img, C[0], C[1], (0, 255, 0), 1)  # C
    cv.putText(img, 'C', ((C[0][0]-30 + C[1][0]) // 2, (C[0][1] + C[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.rectangle(img, Cd[0], Cd[1], (0, 255, 0), 1)  # CD

    cv.rectangle(img,D[0],D[1],(0,255,0),1) # D
    cv.putText(img, 'D', ((D[0][0]-30 + D[1][0]) // 2, (D[0][1] + D[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.rectangle(img,E[0],E[1],(0,255,0),1) # E
    cv.putText(img, 'E', ((E[0][0]-30 + E[1][0]) // 2, (E[0][1] + E[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.rectangle(img,F[0],F[1],(0,255,0),1) # F
    cv.putText(img, 'F', ((F[0][0]-30 + F[1][0]) // 2, (F[0][1] + F[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.rectangle(img,G[0],G[1],(0,255,0),1) # G
    cv.putText(img, 'G', ((G[0][0]-30 + G[1][0]) // 2, (G[0][1] + G[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.rectangle(img,A[0],A[1],(0,255,0),1) # A
    cv.putText(img, 'A', ((A[0][0]-30 + A[1][0]) // 2, (A[0][1] + A[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.rectangle(img, B[0], B[1], (0, 255, 0), 1)  # B
    cv.putText(img, 'B', ((B[0][0]-30 + B[1][0]) // 2, (B[0][1] + B[1][1]) // 2), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


    # Finding landmarks
    lmList = detector.findPos(img, isDraw=False)
    if len(lmList) != 0:
        # Head finger
        x1, y1 = lmList[4][1], lmList[4][2]
        # Pointer finger
        x2, y2 = lmList[8][1], lmList[8][2]
        # Center of line
        centerX, centerY = (x1 + x2) // 2, (y1 + y2) // 2

        cv.circle(img, (x1, y1), 7, (255, 0, 0), cv.FILLED)
        cv.circle(img, (x2, y2), 7, (255, 0, 0), cv.FILLED)
        # cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 5)

        # Distance between points
        dist = math.hypot(math.fabs(x1 - x2), math.fabs(y1 - y2))

        # Touch
        if dist < 30:
            cv.circle(img, (centerX, centerY), 7, (0, 0, 255), cv.FILLED)
            chordAreaControl()
            # if centerX<= C[1][0] :
            #
            #     if C[0][0]<=centerX:
            #
            #         if centerY <= C[1][1]:
            #
            #             if C[0][1] <= centerY:
            #                 # print(('C',centerX,centerY,(C[0][0],C[1][0]),(C[0][1],C[1][1])))
            #                 print('C')

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    cv.imshow('',img)