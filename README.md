# Sentiment Analysis API

This repository contains a Sentiment Analysis API that uses the `cardiffnlp/twitter-roberta-base-sentiment` model from Hugging Face. The API is deployed on Google Cloud AI Platform and provides sentiment predictions for given text inputs.

## Features
- **Pre-trained Model**: Uses `twitter-roberta-base-sentiment` for accurate sentiment classification.
- **Cloud Deployment**: Hosted on Google Cloud AI Platform for scalability and reliability.
- **REST API**: Accepts text input via HTTP requests and returns sentiment predictions.
- **Three Sentiment Classes**:
  - `0`: Negative
  - `1`: Neutral
  - `2`: Positive

## Setup & Deployment
### Prerequisites
Ensure you have the following:
- Google Cloud SDK installed and authenticated
- A Google Cloud project with AI Platform enabled
- Docker installed (if using a custom container)

### Installation
Clone the repository:
```sh
git clone https://github.com/your-username/sentiment-analysis-api.git
cd sentiment-analysis-api
```

## API Usage
Once deployed, you can send requests to the API:
```sh
curl -X POST -H "Content-Type: application/json" \  
     -d '{"text": "I love this product!"}' \  
     [https://your-api-endpoint/predict](https://dashboard.render.com/project/prj-cujq1qt2ng1s73bb1tcg#:~:text=Sentiment_Analysis_Model)
```
### Response Example
```json
{
  "label": "positive",
  "score": 0.98
}
```

## License
This project is licensed under the MIT License.

## Contact
For any issues or suggestions, feel free to open an issue or reach out at [samyakmeshram2020@gmail.com](mailto:samyakmeshram2020@gmail.com).

