from flask import Flask, request

from PIL import Image, ImageOps

import tensorflow as tf
import keras
import numpy as np
np.set_printoptions(threshold=np.inf)

from helpers import FieldNotExistsException, FileNotExistsException, label, reshape_image, romaji

app = Flask(__name__)

model = None

def load_model(file_path: str):
    global model
    model = keras.saving.load_model(file_path)
    model.make_predict_function() # Necessary?

def process_image(img):
    # load image 
    image = Image.open(img).convert("RGBA")
    # app.logger.info(f"Image mode: {image.mode}\nImage dimensions: {image.width} x {image.height}")

    # create white background, same dimensions as original image
    background = Image.new(mode="RGBA", size=(image.width, image.height), color=(255, 255, 255))
    # app.logger.info(f"Background mode: {background.mode}\nImage dimensions: {background.width} x {background.height}")

    # merge layers
    image = Image.alpha_composite(background, image)

    # image.save(secure_filename(img.filename))

    # convert to greyscale
    image = image.convert("L")

    # inverting the image might help with predictions
    image = ImageOps.invert(image)

    # Resize to 48x48
    image = image.resize((48, 48))

    # PIL -> scikit "image"/NumPy array
    img_arr = np.array(image, dtype=np.float32)

    # img_arr = (img_arr / np.max(img_arr)).astype(np.float32)
    img_arr = (img_arr / 255.0).astype(np.float32)

    # make either a 48x48x1 or a 1x48x48
    # NOTE: this may not even be needed! the saved model might need a 48x48x1 input
    return reshape_image(keras.backend.image_data_format(), img_arr)
    # return img_arr

def get_img_from_request(req_data):
    img = req_data.files.get("img", None)

    if img is None:
        raise FieldNotExistsException("Field img does not exist", 400)
    
    if img.filename == "":
        raise FileNotExistsException("No image uploaded", 400)

    return img

@app.route("/predict", methods=["POST"])
def predict():
    try:
        img = get_img_from_request(request)

        # Read file (for debug reasons)
        # app.logger.info(img.read())
        # Save file (for debug reasons)
        # img.save(secure_filename(img.filename))

        # TODO: logic
        img_data = process_image(img)

        # Read processed image data (for debug reasons)
        # app.logger.info(img_data)
        # app.logger.info(f"Image shape: {img_data.shape}")

        pred = model.predict(img_data)
        final_pred = np.argmax(pred[0])
        app.logger.info(f"Prediction(?): {final_pred}")

        return {"romaji": romaji[final_pred], "prediction": label[final_pred]}

    except (FieldNotExistsException, FileNotExistsException) as err:
        return {"message": str(err)}, err.err_code

if __name__ == "__main__": 
    print("Loading Keras model...")
    load_model("models/hiragana_latest.keras")
    app.run(debug=True, host='0.0.0.0') # Add debug = True for logs and stuff
