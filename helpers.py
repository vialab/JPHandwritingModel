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
    # Why the fuck does this exist
    # https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format
    if img_data_fmt == "channels_last":
        img_arr = img_arr.reshape(48, 48, 1)
    else:
        img_arr = img_arr.reshape(1, 48, 48)

    return (np.expand_dims(img_arr, 0))

label = ["あ", "い", "う", "え","お",
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
"ん",]
