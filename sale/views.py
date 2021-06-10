from django.shortcuts import render, redirect

from .models import pclass
from .models import abc
from .models import con


# Create your views here.
def test(request):
    try:
        obj = abc.objects.all()
        return render(request, 'about.html', {'object': obj})

    except:
        return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        first = request.POST['fn']
        second = request.POST['ln']
        pclass.objects.create(head=first, des=second, img=None)
        return render(request, 'register.html')
    else:

        return render(request, 'register.html')


def search(request):
    d = request.GET['search']
    objects = abc.objects.filter(names=d)
    return render(request, 'search.html', {'obj': objects})


def delete(request, id):
    abc.objects.get(id=id).delete()
    return redirect('about')


def detail(request, id):
    obj = abc.objects.get(id=id)
    return render(request, 'detail.html', {'obj': obj})


def update(request, id):
    if request.method == 'POST':
        h = request.POST['form_head']
        d = request.POST['form_des']
        abc.objects.filter(id=id).update(names=h, designations=d)
        return redirect('detail', id=id)
    else:
        obj = abc.objects.get(id=id)
        return render(request, 'update.html', {'obj': obj})


def message(request):
    if request.method == 'POST':
        nam = request.POST['name']
        em = request.POST['email']
        me = request.POST['message']
        con.objects.create(name=nam, email=em, mess=me)
        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')
