

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now


@python_2_unicode_compatible
class Attendee(models.Model):
    student = models.ForeignKey(User, related_name="attendee")

    class Meta:
        verbose_name = 'attendee'
        verbose_name_plural = 'attendees'
        ordering = ['student']

    def __str__(self):
        return self.student

@python_2_unicode_compatible
class Volunteer(models.Model):
    student = models.ForeignKey(User, related_name="volunteer")

    class Meta:
        verbose_name = 'volunteer'
        verbose_name_plural = 'volunteers'
        ordering = ['student']

    def __str__(self):
        return self.student


@python_2_unicode_compatible
class Activity(models.Model):
    type = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="owner")
    college = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    attendee = models.ManyToManyField(Attendee, related_name="attendees",null=True, blank=True)
    volunteer = models.ManyToManyField(Volunteer, related_name="volunteers",null=True, blank=True)
    created_time = models.DateTimeField(editable=False, auto_now= True)
    modified_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        ordering = ['-startDate']

    def __str__(self):
        return '%s (%s)' % (self.title, self.description)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Activity, self).save(*args, **kwargs)