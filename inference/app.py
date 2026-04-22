from flask import Flask, request, jsonify
import joblib
import whisper
from prometheus_client import Counter, start_http_server

app = Flask(__name__)

# métricas
REQUESTS = Counter('request_count', 'Total requests')

# modelo NLP
model, vectorizer = joblib.load("model/model.pkl")

# modelo Whisper
whisper_model = whisper.load_model("base")

@app.route("/analyze", methods=["POST"])
def analyze():
    REQUESTS.inc()

    file = request.files["audio"]
    file.save("temp.wav")

    # transcripción
    result = whisper_model.transcribe("temp.wav")
    text = result["text"]

    # predicción
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    return jsonify({
        "text": text,
        "sentiment": int(pred)
    })

if __name__ == "__main__":
    start_http_server(8000)  # Prometheus
    app.run(host="0.0.0.0", port=5000)