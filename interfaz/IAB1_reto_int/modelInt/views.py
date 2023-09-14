from django.shortcuts import render
from sklearn.metrics import mean_squared_log_error
import joblib
import numpy as np 
from sklearn.ensemble import RandomForestRegressor
from .forms import *
import os
# Create your views here.

# Create your views here.
def home(request):
    #form=Prediction()
    if request.method == "POST":
        form = Prediction(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            pred = np.zeros(51)

            pred[0] = 0
            pred[1] = int(data['ModelStore'])
            pred[2] = int(data['ModelOnp'])
            pred[int(data['ModelFamily'])] = 1 # Change value in the array to 1 in the column of int(data['ModelFamily']
            #p1[50] = 1
            if data['Holidays'] != '0': 
                pred[int(data['Holidays'])] = 1

            path = "D:\\Principal\\Escuela\\Actual\\TEC\\semestre7\\bloque1_IA\\reto_ia\\reto_ia_bloque1\\interfaz\\IAB1_reto_int\modelInt"
            dir_list = os.listdir(path)
            
            
            # prints all files
            print('files:\n',dir_list)
            csv_path = os.path.join(os.path.dirname(__file__), 'randomForestModel.joblib')
            #loaded_rf = joblib.load('interfaz\IAB1_reto_int\modelInt\randomForestModel.joblib')
            loaded_rf = joblib.load(csv_path)
            res = loaded_rf.predict([pred])
            context = {
                "title": "Predecir Ventas",
                "form": form,
                "resultPred": res
            }
            return render(request, "home.html", context)

            

    form=Prediction()
    csv_path = os.path.join(os.path.dirname(__file__), 'randomForestModel.joblib')
            #loaded_rf = joblib.load('interfaz\IAB1_reto_int\modelInt\randomForestModel.joblib')
    loaded_rf = joblib.load(csv_path)
    context = {
        "title": "Predecir Ventas",
        "form": form
    }

    return render(request, "home.html", context)

""""loaded_rf = joblib.load(filename)
loaded_rf.predict([p1])"""