# from django.db import models


# class Activity(models.Model):
#     # question_text = models.CharField(max_length=200)
#     # pub_date = models.DateTimeField('date published')
#     type = models.CharField(max_length=200)
#     time = models.CharField(max_length=200)
#     college = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     room = models.CharField(max_length=200)
#     id = models.CharField(max_length=200)
#     startDate = models.CharField(max_length=200)
#     endDate = models.CharField(max_length=200)
#     coordinatorID = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
   


# class User(models.Model):
#     type = models.ForeignKey(Question, on_delete=models.CASCADE)
#     id = models.CharField(max_length=200)
#     password = models.IntegerField(default=0)
#     email = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)

# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Profile(models.Model):
#     STUDENT = 1
#     TEACHER = 2
#     SUPERVISOR = 3
#     ROLE_CHOICES = (
#         (STUDENT, 'Student'),
#         (TEACHER, 'Teacher'),
#         (SUPERVISOR, 'Supervisor'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

#     def __str__(self):  # __unicode__ for Python 2
#         return self.user.username

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()