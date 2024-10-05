from django.contrib import admin
from .models import Student, Faculty, Contact, Diary, Query, ReplyQuery, AllFaculty, Material, Director

# Register each model to the admin site
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Contact)
admin.site.register(Diary)
admin.site.register(Query)
admin.site.register(ReplyQuery)
admin.site.register(AllFaculty)
admin.site.register(Material)
admin.site.register(Director)