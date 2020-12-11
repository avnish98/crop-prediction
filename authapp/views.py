from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm, ApplicationForm      

from sklearn import preprocessing
from django.conf import settings

# Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVR
import os

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)

def prediction(request):
    forms = ApplicationForm()
    print('form loaded')
    pred = 0
    if request.method == 'POST':
        forms = ApplicationForm(request.POST)
        if forms.is_valid():
            state = forms.cleaned_data['state']
            district = forms.cleaned_data['district']
            category = forms.cleaned_data['category']
            year = forms.cleaned_data['year']
            rainfall = forms.cleaned_data['rainfall']
            temp = forms.cleaned_data['temp']
            area = forms.cleaned_data['area']
            pred = predict([state, district, category, year, rainfall, temp, area])[0]

    else:
        print("A GET REQUEST")
    context = {
        'form': forms,
        'result2':pred
    }
    return render(request, 'result.html', context)

def signout(request):
    logout(request)
    return redirect('signin')


# def result(request):
#     return render(request, "result.html")

def predict(vals):
    my_data = pd.read_csv(os.path.join(settings.BASE_DIR, 'crop_final.csv'))
    state_encodings = dict(zip(my_data['State_Name'].unique(), range(len(my_data['State_Name'].unique()))))
    district_encodings = dict(zip(my_data['District_Name'].unique(), range(len(my_data['District_Name'].unique()))))
    category_encodings = dict(zip(my_data['Category_crop'].unique(), range(len(my_data['Category_crop'].unique()))))

    my_data['State_Name'] = my_data['State_Name'].map(state_encodings)
    my_data['District_Name'] = my_data['District_Name'].map(district_encodings)
    my_data['Category_crop'] = my_data['Category_crop'].map(category_encodings)

    
    # print("DATA LOADED")
    # X_train, X_validation, Y_train, Y_validation = train_test_split(my_data.drop(['Production', 'State_Name', 'District_Name', 'Category_crop'], axis=1), my_data["Production"], test_size=0.30, random_state=1)
    # print("DATA SPLITTED")
    # rf = RandomForestRegressor(max_depth=20, n_estimators=3000)
    rf = LinearRegression()
    rf.fit(my_data.drop('Production', axis=1).values, my_data['Production'].values)
    pred = rf.predict([[state_encodings[vals[0]], district_encodings[vals[1]], category_encodings[vals[2]], vals[3],vals[4],vals[5],vals[6]]])
    return pred
    # print('LOADED MODEL')
    # #rf.score(X_validation, Y_validation)
    # val1 = float(request.GET['Production'])
    # val2 = str(request.GET['State_Name'])
    # val3 = str(request.GET['District_Name'])
    # val4 = str(request.GET['Category_crop'])
    # print('ENCODED DATA')
    # pred = rf.predict([val1,val2,val3,val4])
    # print('PREDICTION DONE')
    # return render(request, "result.html",{"result2:pred"})
