from django.shortcuts import redirect, render
from .models import Text
from .forms import TextForm
# Create your views here.


def index(request):
    q = Text.objects.all()  # get

    form = TextForm()  # post
    context = {'q': q, 'form': form}
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['text']
            w = form.cleaned_data['word']

            if t == '' and w == '':
                print('index: t and w are empty')
                context = {'q': q, 'form': form}
                # return redirect('/')
            elif t == '' and w != '':
                print('index: t are empty')
                z = q.filter(text__contains=w)
                context = {'q': q, 'form': form, 'z': z}
                # return render(request, 'index.html', context)
            elif t != '' and w != '':
                print('None are empty')
                form.save()
                z = q.filter(text__contains=w)
                context = {'q': q, 'form': form, 'z': z}
                # return render(request, 'index.html', context)
            elif t != '' and w == '':
                print('index: W are empty')
                form.save()
                context = {'q': q, 'form': form}
                # return render(request, 'index.html', context)
    return render(request, 'index.html', context)
