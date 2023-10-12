
import streamlit as st
from PIL import Image

# Create a Streamlit app
st.title("Photo Similarity App")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)


camera_picture = st.camera_input("Take a picture")

if camera_picture:
    st.image(camera_picture)
