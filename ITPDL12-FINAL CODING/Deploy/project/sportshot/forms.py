from django import forms 
from . models import UserSportsModel




class UserSportPredictForm(forms.ModelForm):
    
    class Meta:
        model = UserSportsModel
        fields = ['image']