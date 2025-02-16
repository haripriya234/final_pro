from django import forms 
from . models import Players, UserPredictModel



INPUT_CLASSES = 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'

class Players_information_form(forms.ModelForm):

    class Meta:
        model = Players    
        fields = ['first_name','last_name','photo','date_of_birth','nationality','team', 'sports']
        widget = {
            
            'first_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES,
            }),
            'photo':forms.FileInput(attrs={
                'class':INPUT_CLASSES,
            }),
            
            'last_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES,
            }),
            'date_of_birth':forms.DateInput(attrs={
                'class':INPUT_CLASSES,
            }),
            'nationality':forms.Select (attrs={
                'class':INPUT_CLASSES,
            }),
            'team':forms.Select(attrs={
                'class':INPUT_CLASSES,
            }),
            'Sports':forms.Select(attrs={
                'class':INPUT_CLASSES,
            }),
            
        }


class UserPredictForm(forms.ModelForm):
    
    class Meta:
        model = UserPredictModel
        fields = ['image']








    

