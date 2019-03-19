from django.urls import path
#from . import views
from .views import HomePageView, SamplePageviews

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageviews.as_view(), name="sample"),
]
