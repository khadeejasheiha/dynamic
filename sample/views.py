from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    d={
        'head':'company',
         'descrip':'This is a particular website that have all the formatting under the development of an official group'
    }
    return render(request, 'about.html',d)


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')
