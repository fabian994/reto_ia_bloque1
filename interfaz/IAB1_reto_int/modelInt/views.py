from django.shortcuts import render
from sklearn.metrics import mean_squared_log_error
import joblib
import numpy as np 
from sklearn.ensemble import RandomForestRegressor
from forms import *

# Create your views here.

# Create your views here.
def home(request):
    form=Prediction()
    return render(request, "home.html")

""""loaded_rf = joblib.load(filename)
loaded_rf.predict([p1])"""