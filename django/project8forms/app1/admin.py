from django.contrib import admin
from app1.models import student
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail')
#admin.site.register(student,studentadmin)