from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import cv2
import numpy as np

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI application!"} 

@app.post("/is_apple")
async def is_apple(file: UploadFile = File(...)):
    # Read the image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define color range for red apples
    lower_red1 = np.array([0, 100, 100])  # Lower bound for red1
    upper_red1 = np.array([10, 255, 255]) # Upper bound for red1
    lower_red2 = np.array([160, 100, 100]) # Lower bound for red2
    upper_red2 = np.array([180, 255, 255]) # Upper bound for red2

    # Create masks for red apples
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Find contours
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around detected apples (if any contours are found)
    if cnts:
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        print("No contours found. No apples detected.")

    # Save the output image
    cv2.imwrite("output.jpg", img)

    return FileResponse("output.jpg")