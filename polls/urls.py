from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path("<int:question_id>/newchoice/", views.newchoice, name="newchoice"),

    path("<int:question_id>/vote_reset/", views.vote_reset, name="vote_reset"),

    path("addques/", views.addques, name="addques"),

    path("newques/", views.newques, name="newques"),

    path("<int:id>/editques/", views.editques, name="editques"),

   # path("updatques/", views.updatques, name="updatques")

    path("<int:id>/deleteq/", views.deleteq, name="deleteq")
]