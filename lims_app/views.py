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

def delete_reader(request, id):
    try:
        reader_item = reader.objects.get(id=id)
        reader_item.delete()
    except reader.DoesNotExist:
        pass  # Handle case where reader doesn't exist
    return redirect('/readers') 

def update(request, id):
    readers = reader.object.get(id=id)
    return render(request, 'update.html', {"readers":readers})

def update_reader(request, id):
    reader_item = reader.objects.get(id=id)
    if request.method == "POST":
        # Handle form submission
        reader_item.reference_id = request.POST['reader_nim']
        reader_item.reader_name = request.POST['reader_name']
        reader_item.reader_contact = request.POST['reader_contact']
        reader_item.reader_address = request.POST['address']
        reader_item.save()
        return redirect('/readers')
    return render(request, 'update.html', {"reader": reader_item})

def books_tab(request):
    return render(request, "books.html", context={"current_tab": "books"})
