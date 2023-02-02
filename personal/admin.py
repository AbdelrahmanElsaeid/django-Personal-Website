from django.contrib import admin
from .models import About, Services,Experience,Contact,Project,Reviews,Faq

# Register your models here.
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Reviews)
admin.site.register(Faq)
admin.site.register(Contact)
