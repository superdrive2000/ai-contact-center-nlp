import os
import wandb
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

wandb.init(project="call-center-nlp", name="baseline-model")

# =========================
# 1. DATASET (ejemplo)
# =========================
data = pd.DataFrame({
    "text": [
        "Buen dia estimado",
        "Muy buenos dias estimada",
        "me ayudaron rápido",
        "todo perfecto",
        "muy satisfecho",
        "pésimo servicio",
        "no resolvieron mi problema",
        "muy mala experiencia",
        "no me ayudaron",
        "servicio terrible",
        "me atendieron bien",
        "rápido y eficiente",
        "demasiado lento",
        "no solucionaron nada",
        "muchas gracias",
        "horrible atención"
    ],
    "label": [1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0]
})



# =========================
# 2. SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    data["text"], data["label"], test_size=0.25, random_state=42
)

# vectorización simple (para demo)
from sklearn.feature_extraction.text import TfidfVectorizer

# =========================
# 3. VECTORIZACIÓN
# =========================
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# =========================
# 4. MODELO
# =========================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vec, y_train)


# =========================
# 5. PREDICCIÓN
# =========================
y_pred = model.predict(X_test_vec)

# =========================
# 6. MÉTRICAS
# =========================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# =========================
# 7. LOG EN W&B
# =========================
wandb.log({
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1
})

# =========================
# 8. GUARDAR MODELO
# =========================
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Modelo guardado correctamente 💾")

# =========================
# 9. FINALIZAR
# =========================
wandb.finish()