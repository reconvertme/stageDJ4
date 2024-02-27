from django.urls import path
# from .views import listeJournaux
from .views import HomePageView

# urlpatterns = [
#     path("", listeJournaux, name="home"),
# ]
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]