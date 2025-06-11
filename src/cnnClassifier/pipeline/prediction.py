import numpy as np
from tensorflow.keras.models import load_model  #type: ignore
from tensorflow.keras.preprocessing import image #type: ignore
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model(os.path.join("model", "trained_model.h5"))

    def predict(self):
        # Preprocess the input image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0  # Normalize the image
        test_image = np.expand_dims(test_image, axis=0)

        # Perform prediction
        prediction_probs = self.model.predict(test_image, verbose=0)
        print("Prediction probabilities:", prediction_probs)

        result = np.argmax(prediction_probs, axis=1)
        class_names = ["Normal", "Tumor"]  # Adjust based on your training folder structure
        prediction = class_names[result[0]]

        return [{"image": prediction}]