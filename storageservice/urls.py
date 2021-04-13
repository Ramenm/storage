from .views import MainView, TotalCost, DetailView
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    path('recources/', MainView.as_view()),
    path('recources/<int:id>/', DetailView.as_view()),
    path('total_cost/', TotalCost.as_view())
]
