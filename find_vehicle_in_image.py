import tensorflow as tf
from tensorflow.keras.applications import MobileNetV3Large
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

from translate_class_to_vehicle import map_class_to_vehicle

model = MobileNetV3Large(weights='imagenet', input_shape=(224, 224, 3))

def find_vehicle_in_image(image_path):
    def prepare_image(img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array_expanded_dims = np.expand_dims(img_array, axis=0)
        return preprocess_input(img_array_expanded_dims)

    def predict_vehicle(model, prepared_image):
        predictions = model.predict(prepared_image, verbose=0)
        results = decode_predictions(predictions, top=3)[0]

        for _, label, _ in results:
            # Return first result that is a vehicle
            vehicle = map_class_to_vehicle(label)
            if vehicle is not None:
                return vehicle
        
        return None
    
    prepared_image = prepare_image(image_path)
    return predict_vehicle(model, prepared_image)
