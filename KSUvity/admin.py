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

# from django.contrib import admin
# from KSUvity.models import Activity
# # Register your models here.

# admin.site.register(Activity)

from django import forms
from django.contrib import admin

from KSUvity.models import Activity
import datetime

class ActivityAdminForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

    def clean(self):
        if self.cleaned_data['startDate'] > self.cleaned_data['endDate']:
            raise forms.ValidationError('Start Date must be before the End Date')
        if self.cleaned_data['startDate'].date() < datetime.date.today():
            raise forms.ValidationError('The date cannot be in the past!')
        return self.cleaned_data


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityAdminForm


admin.site.register(Activity, ActivityAdmin)