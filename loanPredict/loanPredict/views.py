from django.http import HttpResponse
from django.shortcuts import render
import pickle as pk
import numpy as np
from sklearn.preprocessing import LabelEncoder as le
from sklearn.linear_model import LogisticRegression


def home(request):
    return render(request, 'home.html')

def result(request):

    arr = list(request.POST.get('Credit_History', 'ApplicantIncome', 'LoanAmount','Loan_Amount_Term'))
    arr = np.array([arr])
    arr = arr.astype(float) 
    pickled_model = pk.load(open('model.pkl', 'rb'))
    res = pickled_model.predict(arr)
    params = {'res': res}
    return render(request, 'result.html', params)