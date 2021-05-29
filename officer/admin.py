from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from officer.models import User, Division, Department, Position, Member, Tag, Rank
from officer.models import Profile


admin.site.register(User, UserAdmin)
admin.site.register(Rank)
admin.site.register(Member)
admin.site.register(Position)
admin.site.register(Division)
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(Tag)
