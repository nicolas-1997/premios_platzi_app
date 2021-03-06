from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    #Ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    #Ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #Ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    #Ex: /polls/5/votes/
    path("<int:question_id>/votes/", views.votes, name="votes")
]
