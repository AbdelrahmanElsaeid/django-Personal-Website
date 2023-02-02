from django.shortcuts import render
from .models import About, Services,Experience,Contact,Project,Reviews,Faq
# Create your views here.


def home(request):
    about = About.objects.first()
    experience_first = Experience.objects.all()[:2]
    experience_last = Experience.objects.all()[2:]
    services = Services.objects.all()
    project = Project.objects.all()
    contact = Contact.objects.all()
    faq = Faq.objects.all()
    reviews = Reviews.objects.all()

    return render(request,'home/home.html',
    {
        'about':about,
        'experience_first':experience_first,
        'experience_last':experience_last,
        'faq':faq,
        'contact':contact,
        'services':services,
        'project':project,
        'reviews':reviews,

    })
