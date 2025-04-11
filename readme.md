# Apple Classifier

This is a simple image classifier that predicts the type of apple from an uploaded image using a pre-trained machine learning model. Originally built using FastAPI, this version uses **Streamlit** for easier local deployment and UI.

## Project Structure

```
├── streamlit_app.py         # Main Streamlit web app
├── model/
│   └── apple_classifier.pkl # Trained sklearn model
├── test_images/             # Sample apple images
├── requirements.txt         # Dependencies
```

## Getting Started

### 1. Clone or unzip the repo

```bash
unzip "Fast API Apple guesser.zip"
cd "Fast API Apple guesser"
```

### 2. Install dependencies

We recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
pip install streamlit
```

### 3. Run the Streamlit app

```bash
streamlit run streamlit_app.py
```

### 4. Upload an image to see the predicted apple type 🍏

## Model Info

The model is trained to classify different apple types. It's stored as a `.pkl` file and loaded during runtime.

---

## Sample Predictions

Use the `test_images/` folder to try out sample apple images.

---

## 🤖 Author

Created by Kyle Jackson  
[GitHub](https://github.com/KyleJackson6) | [LinkedIn](https://www.linkedin.com/in/kyle-jackson-1006a52b4/)
