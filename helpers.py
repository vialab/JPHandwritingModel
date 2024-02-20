import numpy as np

class FieldNotExistsException(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code

class FileNotExistsException(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code

def reshape_image(img_data_fmt, img_arr):
    # Apparently Keras has two image data formats???
    # https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format
    if img_data_fmt == "channels_last":
        img_arr = img_arr.reshape(48, 48, 1)
    else:
        img_arr = img_arr.reshape(1, 48, 48)

    # Apparently Keras models are optimized for MULTIPLE predictions instead of single????
    # Create list with one input, apparently
    return (np.expand_dims(img_arr, 0))

label = [
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

romaji = [
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
