from .models import Text   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TextSerializer, WordSerializer, UserSerializer, LoginSerializer
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Login": "/api/login-page/",
        "Logout": "/api/logout-page/",
        "Register": "/api/register-page/",
        
        "GET Get-Paras": "/api/text-list/",
        "POST Post-Paras": "/api/text-upload/",
        "POST Search-Word": "/api/word-search/",
    }
    return Response(api_urls)


@login_required(login_url='login-page')
@api_view(['GET'])
def textList(request):
    texts = Text.objects.all()
    serializer = TextSerializer(texts, many=True)   
    return Response(serializer.data)


@login_required(login_url='login-page')
@api_view(['POST'])
def textUpload(request):
    serializer = TextSerializer(data=request.data)
    data ={}
    if serializer.is_valid():
        text_data = serializer.validated_data['text']
        if text_data == '' or text_data == ' ':
            data['response'] = "Text is empty"
            
        else:
            serializer.save()
            data['response'] = serializer.data
    else:
        data = serializer.errors
    return Response(data)    


@login_required(login_url='login-page')
@api_view(['POST'])
def wordSearch(request):
    q = Text.objects.all()
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        word = serializer.data['word']
        result = q.filter(text__contains=word)
        seri = TextSerializer(result, many=True)
        return Response(seri.data)
    return Response(serializer.errors)

@api_view(['POST'])
def register_page(request):
    serializer = UserSerializer(data=request.data)
    data={}
    if serializer.is_valid():   
        user = serializer.save()
        data['response'] = "Successfully registered a new user."
        data['name'] = user.name
        data['email'] = user.email
        data['dob'] = user.dob
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST',])
def login_page(request):
    serializer = LoginSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        email = serializer.data['email']
        password = serializer.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            data = {'response': 'Successfully logged in.'}
        else:
            print('login: user is not found')
            data = {'response': 'User not found.'}
    return Response(data)


@login_required(login_url='login-page')
@api_view(['GET'])
def logout_page(request):
    logout(request)
    return Response({"Successfully logout"})    