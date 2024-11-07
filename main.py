from typing import Annotated, Any
from fastapi import FastAPI, File, UploadFile
import keras
import numpy as np
from numpy import intp, ndarray
import logging

from classes import FileDoesNotExistHTTPException, FileNotImageHTTPException, PredictionFormResponse
from helpers import load_model, process_image, label, romaji

logger: logging.Logger = logging.getLogger(__name__)
model = load_model("models/hiragana_latest.keras", logger)
app = FastAPI()

@app.get("/ping")
async def get_health() -> dict[str, str]:
    logger.info("Health check accessed")
    return {"status": "OK"}

@app.post("/predict/", response_model=PredictionFormResponse)
async def predict_hiragana_character(img: Annotated[UploadFile, File(media_type="image/png")] | None = File(...)):
    # Check if file is there
    if not img:
        raise FileDoesNotExistHTTPException("No image has been uploaded.")

    # Check if file is even an image
    if not img.content_type.startswith("image/"):
        raise FileNotImageHTTPException(f"File '{img.filename} is not an image.")
    
    file: bytes = await img.read()

    image_data: ndarray = process_image(keras.backend.image_data_format(), file)

    prediction: Any = model.predict(image_data)
    final_prediction: intp = np.argmax(prediction[0])

    logger.info(f"Model predicted {label[final_prediction]} ({romaji[final_prediction]})")
    
    return {
        "romaji": romaji[final_prediction],
        "prediction": label[final_prediction]
    }
