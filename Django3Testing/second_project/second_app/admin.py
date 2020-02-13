from django.contrib import admin
from second_app.models import AccessRecords, Topic, WebPage
# Register your models here.

admin.site.register(AccessRecords)
admin.site.register(Topic)
admin.site.register(WebPage)