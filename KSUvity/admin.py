# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# from KSUvity.authentication.models import Profile

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
from django import forms
from KSUvity.models import Activity
# Register your models here.

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        exclude = ['attendee', 'volunteer', 'modified_time', ]

class ActivityAdmin(admin.ModelAdmin):
    exclude = ['attendee', 'volunteer', 'modified_time', ]
    form = ActivityForm

admin.site.register(Activity, ActivityAdmin)