import cv2
import streamlit as st
from datetime import datetime

now = datetime.now()
day = now.strftime("%A")
hour = now.strftime("%H:%M:%S")

st.title("Motion detctor")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        now = datetime.now()
        day = now.strftime("%A")
        hour = now.strftime("%H:%M:%S")

        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # no cal xd

        cv2.putText(img=frame, text = f"{day}", org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(252, 0, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text = f"{hour}", org=(50,100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(252, 0, 0), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)