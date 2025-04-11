import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("🍎 Apple Guesser")
st.write("Upload an image, and I'll check if it looks like a red apple using color detection!")

uploaded_file = st.file_uploader("Choose an apple image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load and display image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert to OpenCV format
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # Define red HSV ranges
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red detection
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    red_pixels = np.sum(mask > 0)
    total_pixels = mask.size
    red_ratio = red_pixels / total_pixels

    st.write(f"🔍 Red pixel ratio: {red_ratio:.2%}")

    if red_ratio > 0.05:
        st.success("🍎 This is likely a red apple!")
    else:
        st.warning("❌ This doesn't look like a red apple.")
