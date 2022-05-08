from click import style
from rest_framework import serializers
from .models import Text, User
from .forms import TextForm , UserForm

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'
        
        
        
class WordSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=200)
    
class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)  
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'password2', 'dob']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        user = User(
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            dob = self.validated_data['dob'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)    
        user.save()
        return user

{
    "name": "demon",
    "email": "f@g.com",
    "password1": "Sid_8800",
    "password2": "Sid_8800",
    "dob": "2022-02-02"
}
