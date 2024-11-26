from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse
from .models import reader

# Create your views here.
def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

# def readers(request):
#     return render(request, "readers.html", context={"current_tab": "readers","readers":readers})

def shopping(request):
    return HttpResponse("Welcome to Shopping")

def save_student(request):
    student_name = request.POST.get('student_name')
    return render(request, "welcome.html", context={'student_name':student_name})

def readers_tab(request):
    if request.method=="GET":
        readers = reader.objects.all()
        return render(request, "readers.html",
                    context={"current_tab": "readers",
                            "readers":readers})
    else:
        query = request.POST['query']
        readers = reader.objects.raw(
    "SELECT * FROM lims_app_reader WHERE reader_name LIKE %s",
    [f"%{query}%"]
)
        return render(request, "readers.html",
                    context={"current_tab": "readers",
                            "readers":readers,"query":query})

def save_reader(request):
    reader_item = reader (reference_id=request.POST['reader_nim'],
                          reader_name=request.POST['reader_name'],
                          reader_contact=request.POST['reader_contact'],
                          reader_address=request.POST['address'],
                          active=True,
                          )
    reader_item.save()
    return redirect('/readers')
