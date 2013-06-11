from django.db.models import get_models, get_app
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

app_module = get_app('step_game')

for model in get_models(app_module):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
