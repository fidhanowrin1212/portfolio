from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Contact

def home(request):
    projects = Project.objects.all()[:3]  # Show latest 3 projects
    skills = Skill.objects.all()
    return render(request, 'home.html', {'projects': projects, 'skills': skills})

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html')