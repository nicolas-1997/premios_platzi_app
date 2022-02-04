from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    #Ex: /polls/
    path("", views.index, name="index"),
    #Ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    #Ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    #Ex: /polls/5/votes/
    path("<int:question_id>/votes/", views.votes, name="votes")
]
