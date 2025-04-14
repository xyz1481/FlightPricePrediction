from django.shortcuts import render
from .forms import FlightPriceForm
from .models import FlightPricePredictor

def predict_flight_price(request):
    if request.method == 'POST':
        form = FlightPriceForm(request.POST)
        if form.is_valid():
            try:
                predictor = FlightPricePredictor()
                price = predictor.predict(form.cleaned_data)
                
                if price:
                    return render(request, 'predict.html', {
                        'form': form,
                        'prediction': price,
                        'show_result': True
                    })
                
            except Exception as e:
                print(f"Error: {e}")
            
            return render(request, 'predict.html', {
                'form': form,
                'error': 'Prediction failed. Please try different inputs.'
            })
    
    form = FlightPriceForm()
    return render(request, 'predict.html', {'form': form})