from django.db import models

# Create your models here.
class About(models.Model):
    about = models.TextField(max_length=1000)
    logo = models.ImageField(upload_to='logo')
    fb_link = models.URLField(blank=True,null=True)
    tw_link = models.URLField(blank=True,null=True)
    youtube_link = models.URLField(blank=True,null=True)
    instagram_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.about


class Experience(models.Model):
    from_to = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Services(models.Model):
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Project(models.Model):
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to="projects")
     subtitle = models.CharField(max_length=100)
     description = models.TextField(max_length=15000)

     def __str__(self):
        return self.title


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews')
    job_title = models.CharField(max_length=100)
    review = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question        


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.name