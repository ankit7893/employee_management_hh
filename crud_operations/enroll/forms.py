from email.policy import default
from django import forms
from matplotlib import widgets 
from .models import User



class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['name', 'email', 'password']  
        labels = {'name': 'ENTER NAME ' , 'email': 'ENTER EMAIL' , 'password' : 'ENTER PASSWORD' }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={'class':'form-control','autocomplete':'off'}), 
            'password' : forms.PasswordInput( render_value=True ,attrs={'class':'form-control'})
        }


