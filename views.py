from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    return render (request, "home.html")

def about(request):
    return render (request, "about.html")

def projects(request):
    projects_show= [

    {"title": "POS System",
    "path": "images/POS.png"},

    {"title": "Login Form 01",
    "path": "images/Login1.png"},

    {"title": "Login Form 02",
    "path": "images/Login.png"},

    {"title": "Restaurant System",
    "path": "images/food.png"},

    ]
    return render (request, "projects.html",{"projects_show": projects_show})

def experiences(request):
    return render (request, "experiences.html")

def certifications(request):
    return render (request, "certifications.html")

def contact(request):
    return render (request, "contact.html")
       
def resume(request):
    resume_path = "myapp/YabutJohnWalter.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="YabutJohnWalter.pdf"'
            return response
    else:
        return HttpResponse("resume not found", status=404)
        