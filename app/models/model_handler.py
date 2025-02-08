from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define label mapping
label_map = {
    0: "negative",
    1: "neutral",
    2: "positive"
}

def predict_hate_speech(text: str):
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=30,
        return_tensors="pt"
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class_index = torch.argmax(probs).item()
    predicted_label = label_map[predicted_class_index]  # Map index to label
    
    return {
        "prediction": predicted_label,  # Return the label string
        "confidence": float(torch.max(probs)),
        "probabilities": probs.tolist()[0]
    }
