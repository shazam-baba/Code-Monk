from django import forms
from .models import Text, User
from django.contrib.auth.forms import UserCreationForm

class TextForm(forms.ModelForm):
    word = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'required': False, 'placeholder': 'Enter a word'}))

    class Meta:
        model = Text    
        fields = '__all__'  
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'required': False,'placeholder': 'Enter text/Paragraph'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User        
        fields = ['name', 'email', 'password1', 'password2','dob']    
        