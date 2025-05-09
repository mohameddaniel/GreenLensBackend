import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing import image  # type: ignore
import io
from .lables import lables

model = load_model("./Apis/const/model/model_plant.keras")

def predict_image_class(image_file):
    try:
        image_bytes = image_file.read()
        image_stream = io.BytesIO(image_bytes)

        img = image.load_img(image_stream, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])

        return lables[predicted_index] ,predictions[0][predicted_index]
    
    except Exception as e:
        print("Erreur lors de la prédiction :", str(e))
        return "Erreur de prédiction"
