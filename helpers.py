import logging
from typing import Any
import keras
import numpy as np
from PIL import Image, ImageOps

def load_model(filepath: str, logger: logging.Logger) -> Any: # that's what keras said the model was
    model = keras.saving.load_model(filepath)
    model.make_predict_function() # Is this necessary?

    logger.info(f"Model from {filepath} loaded successfully")

    return model

def process_image(img_data_fmt, img) -> np.ndarray:
    # load image and create fully white background based on image dimensions
    image: Image.Image = Image.open(img).convert("RGBA")
    background: Image.Image = Image.new(mode="RGBA", size=(image.width, image.height), color=(255, 255, 255))
    image = Image.alpha_composite(background, image) # merge the images

    # more image filtering
    image = image.convert("L") # convert to greyscale
    image = ImageOps.invert(image) # might help with predictions

    image = image.resize((48, 48)) # resize to expected input dimensions

    img_arr: np.ndarray = np.array(image, dtype=np.float32)
    img_arr = (img_arr / 255.0).astype(np.float32)

    # make either a 48x48x1 or a 1x48x48
    return reshape_image(img_data_fmt, img_arr)

def reshape_image(img_data_fmt, img_arr) -> np.ndarray:
    # Apparently Keras has two image data formats???
    # https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format
    if img_data_fmt == "channels_last":
        img_arr = img_arr.reshape(48, 48, 1)
    else:
        img_arr = img_arr.reshape(1, 48, 48)

    # Keras is meant for multiple files, so make an array with one element
    return (np.expand_dims(img_arr, 0))

label: list[str] = [
    "あ", "い", "う", "え", "お",
    "か", "が", "き", "ぎ", "く",
    "ぐ", "け", "げ", "こ", "ご", 
    "さ", "ざ", "し", "じ", "す",
    "ず", "せ", "ぜ", "そ", "ぞ",
    "た", "だ", "ち", "ぢ", "つ",
    "づ", "て", "で", "と", "ど",
    "な", "に", "ぬ", "ね", "の",
    "は", "ば", "ぱ", "ひ", "び",
    "ぴ", "ふ", "ぶ", "ぷ", "へ",
    "べ", "ぺ", "ほ", "ぼ", "ぽ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ", "ら", "り",
    "る", "れ", "ろ", "わ", "を",
    "ん"
]

romaji: list[str] = [
    "a", "i", "u", "e", "o",
    "ka", "ga", "ki", "gi", "ku",
    "gu", "ke", "ge", "ko", "go",
    "sa", "za", "shi", "ji", "su",
    "zu", "se", "ze", "so", "zo",
    "ta", "da", "chi", "ji", "tsu",
    "zu", "te", "de", "to", "do",
    "na", "ni", "nu", "ne", "no",
    "ha", "ba", "pa", "hi", "bi",
    "pi", "fu", "bu", "pu", "he",
    "be", "pe", "ho", "bo", "po",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo", "ra", "ri",
    "ru", "re", "ro", "wa", "wo",
    "n"
]
