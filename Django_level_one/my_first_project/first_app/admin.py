from django.contrib import admin

# Register your models here.
from first_app.models import AccessRecord,Webpage,Topic
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
