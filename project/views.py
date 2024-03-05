from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

# Create your views here.
def home(request):
    return render(request, 'index.html')



def calculate(request):
    df = pd.read_csv('csv_file/Project_Data.csv')
    df.columns = ['StudyHours', 'GotMarks']
    X = df[['StudyHours']]  
    y = df['GotMarks']  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    
    sample_result = df.sample(5)

    print(sample_result)

    result = "Enter study hours to predict marks"
    if request.method == 'POST':
        hrs = float(request.POST.get('hours'))
        if hrs is None:
            result = "Value should not be none!!"
        else:
            study_hours = [[(hrs)]]  
            predicted_marks = regressor.predict(study_hours)
            print(f"Predicted marks for study hours of {hrs}:", predicted_marks[0])
            result = predicted_marks[0]

    context = {
        'sample_result': sample_result.to_dict("records"),
        'result': result, 
        'hrs': hrs,
    }
    return render(request, 'result.html', context)

# def calculate(request):
#     df = pd.read_csv('csv_file/Project_Data.csv')
#     df.columns = ['StudyHours', 'GotMarks']
#     X = df[['StudyHours']]  # Features
#     y = df['GotMarks']  # Target variable
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#     regressor = LinearRegression()  
#     regressor.fit(X_train, y_train)

#     result = 0
#     if request.method == 'POST':
#         hrs = float(request.POST.get('hours'))
#         if hrs is None:
#             result = "Value should not be none!!"
#         else:
#             study_hours = [[hrs]]  
#             predicted_marks = regressor.predict(study_hours)
#             print(f"Predicted marks for study hours of {hrs}:", predicted_marks[0])
#             result = predicted_marks[0]
#     return render(request, 'result.html', {'result': result})
