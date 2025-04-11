import streamlit as st
import pickle
from PIL import Image
import numpy as np
import cv2

# Load model
with open("model/apple_classifier.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🍎 Apple Guesser")
st.write("Upload an image of an apple, and I'll guess the type!")

uploaded_file = st.file_uploader("Choose an apple image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocessing (make sure this matches what model expects)
    img_array = np.array(image)
    img_resized = cv2.resize(img_array, (100, 100)).flatten().reshape(1, -1)

    prediction = model.predict(img_resized)
    st.subheader(f"🔮 Predicted Apple Type: {prediction[0]}")
