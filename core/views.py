from django.shortcuts import render, redirect
from .models import About, Skill, Education, Experience, Service, ContactMessage
from django.contrib import messages

# -----------------------------
# Home / Index Page
# -----------------------------
def index(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    services = Service.objects.all()
    
    context = {
        'about': about,
        'skills': skills,
        'education': education,
        'experience': experience,
        'services': services,
    }
    return render(request, 'index.html', context)

# -----------------------------
# Contact Form Submission
# -----------------------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')  # redirect to homepage after submission

    return redirect('index')  # fallback redirect if not POST
