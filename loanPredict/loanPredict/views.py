from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

import pickle as pk
import numpy as np
from sklearn.preprocessing import LabelEncoder as le
from sklearn.linear_model import LogisticRegression


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def result(request):

    Credit_History = request.POST.get('Credit_History')
    ApplicantIncome = request.POST.get('ApplicantIncome')
    LoanAmount = request.POST.get('LoanAmount')
    Loan_Amount_Term = request.POST.get('Loan_Amount_Term')
    arr = [Credit_History, ApplicantIncome, LoanAmount, Loan_Amount_Term]
    print(arr)
    arr1 = str(request.POST.get('Name'))
    arr = np.array([arr])
    arr = arr.astype(float) 
    pwd = os.path.dirname(__file__)
    pickled_model = pk.load(open(pwd+'/finalized_model.sav', 'rb'))
    res = pickled_model.predict(arr)
    
    print(res)
    
    res1 = ''
    res2 = ''
    
    if res == [1]:
        res1 = 'Approved'
        res2 = 'Click on get started to get yourself registered'
    else:
        res1 = 'Denied'
        res2 = 'Try Again !'
    
    params = {'res1': res1, 'res2' : res2,'Name': arr1}
    return render(request, 'result.html', params)
   # ApplicantIncome, LoanAmount,Loan_Amount_Term