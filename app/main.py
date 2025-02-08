from fastapi import FastAPI
from app.models.model_handler import predict_hate_speech
from app.schemas import TextInput, PredictionOutput

app = FastAPI(title="Hate Speech Detection API")
@app.get("/")
async def initialize():
    return {"message": "Hate Speech Detection API"}
@app.post("/predict", response_model=PredictionOutput)
async def predict_endpoint(input_data: TextInput):
    """Endpoint for hate speech detection"""
    return predict_hate_speech(input_data.text)
