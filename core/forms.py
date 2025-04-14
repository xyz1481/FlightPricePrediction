from django import forms

AIRLINE_CHOICES = [
    ('SpiceJet', 'SpiceJet'),
    ('AirAsia', 'AirAsia'),
    ('Vistara', 'Vistara'),
    ('GO_FIRST', 'GO FIRST'),
    ('Indigo', 'Indigo'),
    ('Air_India', 'Air India'),
]

CITY_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Kolkata', 'Kolkata'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
]

TIME_CHOICES = [
    ('Early_Morning', 'Early Morning (12AM-6AM)'),
    ('Morning', 'Morning (6AM-12PM)'),
    ('Afternoon', 'Afternoon (12PM-6PM)'),
    ('Evening', 'Evening (6PM-12AM)'),
]

CLASS_CHOICES = [
    ('Economy', 'Economy'),
    ('Business', 'Business'),
]

class FlightPriceForm(forms.Form):
    airline = forms.ChoiceField(choices=AIRLINE_CHOICES)
    source_city = forms.ChoiceField(choices=CITY_CHOICES)
    departure_time = forms.ChoiceField(choices=TIME_CHOICES)
    stops = forms.IntegerField(min_value=0, max_value=2)
    arrival_time = forms.ChoiceField(choices=TIME_CHOICES)
    destination_city = forms.ChoiceField(choices=CITY_CHOICES)
    flight_class = forms.ChoiceField(choices=CLASS_CHOICES)
    duration = forms.FloatField(min_value=1.0)
    days_left = forms.IntegerField(min_value=1)