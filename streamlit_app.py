import streamlit as st
import cv2




st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# Check OpenCV version
st.write("OpenCV version:")
print("heyy!")
st.write(cv2.__version__)
