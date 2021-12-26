from django.contrib import admin
from .models import score , scores_date ,home_goal_scorers , away_goal_scorers
# Register your models here.
admin.site.register(scores_date)
admin.site.register(score)
admin.site.register(home_goal_scorers)
admin.site.register(away_goal_scorers)