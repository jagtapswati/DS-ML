from django.shortcuts import render
import joblib
import pandas as pd
import numpy as np

# Create your views here.
def index(request):
    if request.method == "POST":
        yrs = request.POST['yrs']
        yrs = float(yrs)
        print(yrs,type(yrs))
        loaded_model = joblib.load('model/salary_prediction_model.pkl')
        predicted_salary = loaded_model.predict(np.array([[yrs]]))
        print(predicted_salary[0])
        
    return render(request,'index.html')
    
    
def log_in(request):
    return render(request,'login.html')
    