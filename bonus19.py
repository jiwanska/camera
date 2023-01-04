import streamlit as st

from PIL import Image

st.subheader("Color to grayscale Converter")

upload_image = st.file_uploader("Upload your image")

with st.expander("Start Camera"):
    #start camera
    camera_image = st.camera_input("Camera")


if camera_image:
    #create a pillow image instance
    img = Image.open(camera_image)

    #convert the pillow image to grayscale
    gray_img = img.convert("L")

    #render the greyscale on the webpage
    st.image(gray_img)

if upload_image:
    img = Image.open(upload_image)

    gray_img = img.convert("L")

    st.image(gray_img)