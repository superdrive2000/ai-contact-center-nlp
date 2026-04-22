from flask import Flask, request, jsonify,  render_template
import joblib
import whisper
from prometheus_client import Counter, start_http_server

app = Flask(__name__)

# métricas
REQUESTS = Counter('request_count', 'Total requests')

# modelo NLP
model, vectorizer = joblib.load("model/model.pkl")

# modelo Whisper
whisper_model = whisper.load_model("small")

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
    
    
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze-ui", methods=["POST"])
def analyze_ui():
    REQUESTS.inc()

    file = request.files["audio"]
    file.save("temp.wav")

    # transcripción
    result = whisper_model.transcribe("temp.wav")
    text = result["text"]

    # predicción
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    sentiment_label = "positivo" if pred == 1 else "negativo"

    return render_template(
        "index.html",
        text=text,
        sentiment=sentiment_label
    )


if __name__ == "__main__":
    start_http_server(8000)  # Prometheus
    app.run(host="0.0.0.0", port=5000)