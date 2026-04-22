import pandas as pd
import wandb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

wandb.init(project="call-center-nlp")

# dataset de ejemplo
data = pd.DataFrame({
    "text": [
        "muy buena atención",
        "pésimo servicio",
        "me ayudaron rápido",
        "no resolvieron mi problema"
    ],
    "label": [1, 0, 1, 0]
})

X_train, X_test, y_train, y_test = train_test_split(
    data["text"], data["label"], test_size=0.2
)

# vectorización simple (para demo)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = RandomForestClassifier()
model.fit(X_train_vec, y_train)

# guardar modelo
joblib.dump((model, vectorizer), "model.pkl")

wandb.log({"status": "trained"})