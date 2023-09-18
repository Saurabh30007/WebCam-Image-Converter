# This is a Python script, which takes a picture from the web camera
# and converts into a gray scale picture


import streamlit as st
from PIL import Image


# Create a file uploader component allowing the user to upload a file
upload_image = st.file_uploader('Upload Image')

# Check if the image exists meaning the user has uploaded a file
if upload_image:
    up_img = Image.open(upload_image)
    up_gray_image = up_img.convert('L')
    st.image(up_gray_image)


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


# to run this application write 'streamlit run main.py' in the terminal section
