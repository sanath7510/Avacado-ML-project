
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

def load_model():
    data = pd.read_csv("avocado_ripeness_dataset.csv")

    color_enc = LabelEncoder()
    data['color_category'] = color_enc.fit_transform(data['color_category'])

    target_enc = LabelEncoder()
    data['ripeness'] = target_enc.fit_transform(data['ripeness'])

    X = data[['firmness','hue','saturation','brightness',
              'color_category','sound_db','weight_g','size_cm3']]
    y = data['ripeness']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = SVC(kernel='rbf', C=10, gamma='scale')
    model.fit(X_scaled, y)

    return model, scaler, color_enc, target_enc
