from django.contrib import admin
from . models import Players, Teams, Sports, Nationalities, UserPredictModel



admin.site.register(Players)
admin.site.register(Teams)
admin.site.register(Sports)
admin.site.register(Nationalities)
admin.site.register(UserPredictModel)

