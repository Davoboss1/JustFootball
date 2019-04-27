from django.contrib import admin
from .models import *




#from .models import europe_competitions, africa_competitions ,
#north_america_competitions,south_america_competitions,asia_competitions,australia_competitions,others_competitions
# Regiser your models here.
admin.site.register(Standings)

admin.site.register(Table)
admin.site.register(europe_competitions)
admin.site.register(africa_competitions)
admin.site.register(north_america_competitions)
admin.site.register(south_america_competitions)
admin.site.register(asia_competitions)
admin.site.register(australia_competitions)
admin.site.register(others_competitions)


