import joblib
import os
import numpy as np
from django.conf import settings

class FlightPricePredictor:
    def __init__(self):
        model_path = os.path.join(settings.BASE_DIR, 'core', 'models', 'flight_price_rf_model.pkl')
        model_data = joblib.load(model_path)
        self.model = model_data['model']
        self.encoders = model_data['encoders']
        self.feature_order = model_data['feature_order']
    
    def predict(self, form_data):
        try:
            # Prepare and encode features
            features = {}
            features['airline'] = self._encode('airline', form_data['airline'])
            features['source_city'] = self._encode('source_city', form_data['source_city'])
            features['destination_city'] = self._encode('destination_city', form_data['destination_city'])
            features['class'] = self._encode('class', form_data['flight_class'])
            features['departure_time'] = self._encode('departure_time', form_data['departure_time'])
            features['arrival_time'] = self._encode('arrival_time', form_data['arrival_time'])
            features['duration'] = float(form_data['duration'])
            features['stops'] = int(form_data['stops'])
            features['days_left'] = int(form_data['days_left'])
            
            # Order features correctly
            ordered_features = [features[col] for col in self.feature_order]
            
            # Predict
            prediction = self.model.predict([ordered_features])[0]
            return max(round(prediction, 2), 1000)  # Ensure minimum price
        except Exception as e:
            print(f"Prediction error: {e}")
            return None
    
    def _encode(self, feature_name, value):
        return self.encoders[feature_name].transform([str(value)])[0]