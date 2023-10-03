from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('pages/', views.home, name='home.main'),
    path('pages/portfolio/<int:pk>', views.portfolio_details, name='portfolio.details'),
    path('', RedirectView.as_view(url='pages/')),
    path('pages/download/', views.download_cv, name="download.cv")
]
