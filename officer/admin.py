from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from officer.models import User, Division, Department, Position, MemberProfile, Success
from officer.models import Destination


class ProfileInline(admin.StackedInline):
    model = MemberProfile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'title',
        'first_name',
        'last_name',
        'nick_name',
        'phone',
        'birth_date',
        'profile_picture',
        'position',
        'department',

    )
    list_select_related = ('profile',)

    def get_department(self, instance):
        return instance.profile.department
    get_department.name = 'Department'

    def get_position(self, instance):
        return instance.profile.position
    get_position.name = 'Position'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)
admin.site.register(MemberProfile)
admin.site.register(Position)
admin.site.register(Division)
admin.site.register(Department)
admin.site.register(Success)
