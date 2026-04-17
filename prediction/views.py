from django.shortcuts import render
import numpy as np
from .svm_model import load_model

# Load model once
model, scaler, color_enc, target_enc = load_model()


def home(request):
    result = None

    if request.method == "POST":
        vals = [
            float(request.POST["firmness"]),
            float(request.POST["hue"]),
            float(request.POST["saturation"]),
            float(request.POST["brightness"]),
            color_enc.transform([request.POST["color"]])[0],
            float(request.POST["sound_db"]),
            float(request.POST["weight"]),
            float(request.POST["size"]),
        ]

        arr = scaler.transform([vals])
        prediction = model.predict(arr)[0]
        result = target_enc.inverse_transform([prediction])[0]

    return render(
        request,
        "index.html",
        {"result": result, "colors": color_enc.classes_},
    )