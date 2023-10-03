from django.db import models


# Home table
class Home(models.Model):
    # Django creates a Primary key upon creating a model class usually in integer format
    # Hi! I'm Ian
    greet = models.CharField(max_length=20)
    # Cover Pic (rename your cover picture as "hero-bg.jpg" before uploading)
    coverPic = models.ImageField(upload_to='static/img/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.greet


# make a relationship with Home Table
class MyTitles(models.Model):
    # create a foreign key to Home table primary key
    fkTitle = models.ForeignKey(Home, on_delete=models.CASCADE)
    # MyTitles table fields (column)
    # This will show "typed" text in the cover picture (i.e. Django Developer...)
    myJobs = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)


# for profile pic
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='static/img/')
    updated = models.DateTimeField(auto_now=True)

    
# About
class About(models.Model):
    aboutDescSec = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.aboutDescSec


# Skills table
class Skills(models.Model):
    skillsName = models.CharField(max_length=20)
    skillsURL = models.URLField()
    skillsImg = models.ImageField(upload_to="static/img/")
    
    def __str__(self):
        return self.skillsName


class Portfolio(models.Model):
    portLabel = models.CharField(max_length=50)
    portLabelDesc = models.TextField()
    portCoverImg = models.ImageField(upload_to='static/img')
    isActive = models.BooleanField(default=False)
    portURL = models.URLField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.portLabel


class PortDetailsImg(models.Model):
    fkPortfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    portImg = models.ImageField(upload_to="static/img/")
    updated = models.DateTimeField(auto_now=True)
    

class Contact(models.Model):
    CV = models.FileField(upload_to="static/cv")
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

