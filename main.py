# This is a Python script, which takes a picture from the web camera
# and converts into a gray scale picture


import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    # Starting the camera
    camera_image = st.camera_input('Camera')

if camera_image:
    # Creating a pillow image instance
    img = Image.open(camera_image)

    # Converting the pillow image in grayscale
    gray_image = img.convert('L')

    # Rendering the grayscale image on the webpage
    st.image(gray_image)
