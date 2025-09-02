import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from model.cnn_model import build_cnn_model
from prediction.advice import get_advice

# Injury categories
CATEGORIES = [
    "bleeding",
    "fracture",
    "burn",
    "allergic reaction",
    "choking",
    "dog bite",
    "electrical injuries",
    "cat claw",
    "mosquito bite",
    "normal"
]

def predict_image(model, img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    predicted_class = CATEGORIES[np.argmax(predictions)]
    return predicted_class, confidence

def predict_text(user_text):
    # Simple rule-based system for contextual input
    rules = {
        "bleeding": ["cut", "bleeding", "blood"],
        "fracture": ["broken bone", "fracture", "crack"],
        "burn": ["burn", "fire", "scald"],
        "allergic reaction": ["rash", "allergic", "swelling"],
        "choking": ["choke", "choking", "can't breathe"],
        "dog bite": ["dog bite", "bitten by dog"],
        "electrical injuries": ["electric", "shock", "electrocute"],
        "cat claw": ["cat scratch", "claw"],
        "mosquito bite": ["mosquito", "bite"],
        "normal": ["fine", "okay", "no injury"]
    }

    for injury, keywords in rules.items():
        for keyword in keywords:
            if keyword in user_text.lower():
                return injury, 0.9  # high confidence for rule-based
    return "unknown", 0.3
