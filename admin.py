from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorials, TutorialCategory,TutorialSeries
from .models import PythonNews
# Register your models here.
class TutorialsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget': TinyMCE()}
    }
admin.site.register(Tutorials, TutorialsAdmin)
class PythonNewsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget': TinyMCE()}
    }
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)

