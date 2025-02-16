from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Players
from .forms import Players_information_form
import numpy as np
import joblib
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect
from . models import UserPredictModel
from . forms import UserPredictForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np

from tensorflow import keras
from PIL import Image, ImageOps
from . import forms

from sklearn.metrics import precision_recall_curve
from django.shortcuts import render
from django.core.mail import EmailMessage
from . models import UserPredictModel



def landing_page(request):
    return render(request, 'app/1_landingpage.html')

@login_required(login_url='userlogin')
def index(request):
    return render(request, 'app/3_index.html')

@login_required(login_url='userlogin')
def problem_statement(request):
    return render(request, 'app/info_sport.html')


# This is personal information form submission
@login_required(login_url='userlogin')
def player_information(request):
    
    if request.method == 'POST':
        print('Data is valid')
        form = Players_information_form(request.POST, request.FILES)
        if form.is_valid():
            print('Personal form is valid')
            form.save()
            return redirect('player_dashboard')
    else:
        form = Players_information_form()      
    return render(request, 'app/5_personal_information.html', {'form':form})

@login_required(login_url='userlogin')
def team(request):
    return render(request, 'app/6_team.html')

@login_required(login_url='userlogin')
def sport_shot_database(request):
    models = UserPredictModel.objects.all()
    return render(request, 'app/sport_shot_database.html', {'models': models})



def sport_shot_model(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserPredictForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserPredictModel.objects.latest('id')
        models = keras.models.load_model('E:/IYYAPPAN/ITPDL12-FINAL/ITPDL12-FINAL CODE/Deploy/project/app/sport_shot.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("E:/IYYAPPAN/ITPDL12-FINAL/ITPDL12-FINAL CODE/Deploy/project/media/images/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['Address_for_golf','Drive_for_cricket','Finish_for_golf','Impact_for_golf','legglance_flick_for_cricket', 'Mid-Backswing_for_golf', 'Mid-Downswing_for_golf', 'Mid-Follow-Through_for_golf', 'pullshot_for_cricket', 'sweep_for_cricket', 'Toe-up_for_cricket', 'Top_for_golf']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == 'Address_for_golf':
            print(a)
            a = 'Address_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Drive_for_cricket':
            print(a)
            a = 'Drive_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Finish_for_golf':
            print(a)
            a = 'Finish_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Impact_for_golf':
            print(a)
            a = 'Impact_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'legglance_flick_for_cricket':
            print(a)
            a = 'legglance_flick_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Mid-Backswing_for_golf':
            print(a)
            a = 'Mid-Backswing_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Mid-Downswing_for_golf':
            print(a)
            a = 'Mid-Downswing_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Mid-Follow-Through_for_golf':
            print(a)
            a = 'Mid-Follow-Through_for_golf.'
            b = 'Shot represent in Golf sports'
        
        elif a == 'pullshot_for_cricket':
            print(a)
            a = 'pullshot_for_cricket'
            b = 'Shot represent in Cricket sports'
        
        elif a == 'sweep_for_cricket':
            print(a)
            a = 'sweep_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Toe-up_for_cricket':
            print(a)
            a = 'Toe-up_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Top_for_golf':
            print(a)
            a = 'Top_for_golf'
            b = 'Shot represent in Golf sports'
       
        data = UserPredictModel.objects.latest('id')
        data.label = a
        data.save()

        
        return render(request, 'app/sport_shot_output.html',{'form':form,'obj':obj,'predict':a,'des':b})
    else:
        form = forms.UserPredictForm()
    return render(request, 'app/sports_shot_model.html',{'form':form})



@login_required(login_url='Authorlogin')
def player_dashboard(request):
    users = Players.objects.all()
    context = {
        'users': users,
        }
    return render(request, 'app/player_database.html', context)


@login_required(login_url='Authorlogin')
def player_database(request):
    users = Players.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'auth/3_Database.html', context)




