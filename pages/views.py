from django.shortcuts import render, get_object_or_404
from django.http import Http404, FileResponse
from .models import Home, MyTitles, Profile, About, Skills, Contact, Portfolio, PortDetailsImg


def home(request):
    # You can change the profile pic
    # will automatically replace profile pic to the latest uploaded image

    profilePic = Profile.objects.latest('updated')

    # get content of Home model from model.py
    # You can change what you want to display as greetings (ex: "Hi I'm Ian")
    home_content = Home.objects.latest('updated')
    
    # get list of jobs (select *)
    title_content = MyTitles.objects.all()
    
    # About section
    about = About.objects.latest('updated')
    # about = About.objects.all()
    s = ', '.join([str(record.myJobs) for record in title_content])
    
    # Skills section
    skills = Skills.objects.all()

    # Contacts section
    contact = Contact.objects.latest('updated')


    # Portfolio displayed in carousel
    portfolios = Portfolio.objects.all()


    content = {
        "profilePic":profilePic,
        "home_content":home_content,
        "jobs_content":s,
        "about":about,
        "skills":skills,
        "contact":contact,
        "portfolio":portfolios
    }
    
    return render(request, "pages/index.html", content)


def portfolio_details(request, pk):
    try:    
        pkey = Portfolio.objects.get(pk=pk)
    except Portfolio.DoesNotExist:
        raise Http404("Opps! nothing to view here :(")
    profilePic = Profile.objects.latest('updated')
    portfolios = Portfolio.objects.all()
    # get images from PortDetailsImg model referencing the portfolio primary key
    # fkPortfolio -> pk of Portfolio model
    portImages = PortDetailsImg.objects.filter(fkPortfolio__pk=pk)
    return render(request, "pages/portfolio-details.html",{"details":pkey,
                                                           "profilePic":profilePic,
                                                            "portfolio":portfolios,
                                                            "portImages":portImages
                                                            })

def download_cv(request):
    get_cv = Contact.objects.latest('updated')
    response = FileResponse(get_cv.CV, as_attachment=True)
    return response