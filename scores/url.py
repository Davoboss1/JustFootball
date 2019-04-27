from django.urls import path
from . import views

app_name = "scores"

urlpatterns = [
path("scores/",views.scores,name="scores"),
path("scores/<int:year>/<week>/",views.scores.as_view(),name="scores"),
path("scores/add_scores_date/",views.add_scores_dates,name="add_scores_date"),
path("scores/add_scores/",views.add_scores.as_view(),name="add_scores"),
path("scores/update_scores/",views.update_scores_url,name="update_scores_url"),
path("scores/update_scores/<int:pk>/",views.update_scores.as_view(),name="update_scores"),
path("scores/update_scores/",views.update_scores_url,name="update_scores"),
path("scores/delete_scores/",views.delete_scores_url,name="delete_scores_url"),
path("scores/delete_scores/<int:pk>/",views.delete_scores.as_view(),name="delete_scores"),
path('scores/goal_scorers/<int:score_id>/',views.goal_scorers,name="goal_scorers"),
path('scores/goal_scorers/',views.goal_scorers,name="goal_scorers"),


]


