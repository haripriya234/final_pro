from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

import numpy as np
import joblib
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect

from . forms import UserSportPredictForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
from tensorflow import keras
from PIL import Image, ImageOps
from . import forms
from sklearn.metrics import precision_recall_curve
from django.shortcuts import render
from django.core.mail import EmailMessage
from . models import UserSportsModel




@login_required(login_url='userlogin')
def sport_model(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserSportPredictForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserSportsModel.objects.latest('id')
        models = keras.models.load_model('E:/IYYAPPAN/ITPDL12-FINAL/ITPDL12-FINAL CODE/Deploy/project/sportshot/sport.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("E:/IYYAPPAN/ITPDL12-FINAL/ITPDL12-FINAL CODE/Deploy/project/media/images/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['badminton','basketball','boxing','chess','cricket','fencing', 'football', 'formula1','gymnastics', 'hockey', 'kabaddi', 'motogp', 'shooting', 'swimming', 'table_tennis', 'tennis', 'volleyball', 'weight_lifting', 'wrestling', 'wwe']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])

        if a == 'badminton':
            a = 'badminton'
            print(a)

        elif a == 'basketball':
            a = 'basketball'
            print(a)
            
        elif a == 'boxing':
            a = 'boxing'
            print(a)

        elif a == 'chess':
            a = 'chess'
            print(a)

        elif a == 'cricket':
            a = 'cricket'
            print(a)
        
        elif a == 'fencing':
            a = 'fencing'
            print(a)

        elif a == 'football':
            a = 'football'
            print(a)

        elif a == 'formula1':
            a = 'formula1'
            print(a)

        elif a == 'gymnastics':
            a = 'gymnastics'
            print(a)

        elif a == 'hockey':
            a = 'hockey'
            print(a)

        elif a == 'kabaddi':
            a = 'kabaddi'
            print(a)

        elif a == 'motogp':
            a = 'motogp'
            print(a)

        elif a == 'shooting':
            a = 'shooting'
            print(a)

        elif a == 'swimming':
            a = 'swimming'
            print(a)

        elif a == 'table_tennis':
            a = 'table_tennis'
            print(a)

        elif a == 'tennis':
            a = 'tennis'
            print(a)

        elif a == 'volleyball':
            a = 'volleyball'
            print(a)

        elif a == 'weight_lifting':
            a = 'weight_lifting'
            print(a)

        elif a == 'wrestling':
            a = 'wrestling'
            print(a)

        elif a == 'wwe':
            a = 'wwe'
            print(a)

    
       

        data = UserSportsModel.objects.latest('id')
        data.label = a
        data.save()

        
        return render(request, 'sports_output.html',{'form':form,'obj':obj,'predict':a})
    else:
        form = forms.UserSportPredictForm()
    return render(request, 'sports_model.html',{'form':form})

@login_required(login_url='userlogin')
def sport_database(request):
    models = UserSportsModel.objects.all()
    return render(request, 'app/sport_database.html', {'models':models})


