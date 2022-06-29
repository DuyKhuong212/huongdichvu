from django.contrib import admin
from .models import Award, FormApply, User, StudentTranscript
# Register your models here.
admin.site.register(User)
admin.site.register(Award)
admin.site.register(FormApply)
admin.site.register(StudentTranscript)