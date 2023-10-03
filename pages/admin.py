from django.contrib import admin
from .models import Profile, Home, MyTitles, About, Skills, Portfolio, PortDetailsImg, Contact


# Make tabular entry for Home table
class My_titles(admin.TabularInline):
     model = MyTitles
     extra = 1
     

@admin.register(Home)
class Home_titles(admin.ModelAdmin):
    inlines = [My_titles]


class Port_detailsImg(admin.TabularInline):
     model = PortDetailsImg
     extra = 1

@admin.register(Portfolio)
class Portfolio_details(admin.ModelAdmin):
     inlines = [Port_detailsImg]


admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(About)
admin.site.register(Contact)