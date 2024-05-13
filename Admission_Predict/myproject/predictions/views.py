# predictions/views.py

from django.shortcuts import render
from .forms import ScoreForm
from .utils import model, university_inverse_mapping
import numpy as np

def predict(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            university_code = university_inverse_mapping.get(data['university'], -1)
            new_data = np.array([[
                data['korean_score'], data['english_score'], data['math_score'],
                data['korean_grade'], data['english_grade'], data['math_grade'],
                university_code
            ]])
            prediction = model.predict(new_data)
            result = prediction[0][0] * 100
            return render(request, 'result.html', {'result': result})
    else:
        form = ScoreForm()
    return render(request, 'index.html', {'form': form})
