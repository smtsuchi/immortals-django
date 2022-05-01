from secrets import choice
from django.db import models

# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    how_did_you_hear = models.CharField(max_length=255)
    what_attracted_you = models.CharField(max_length=255)
    interest_in_lion_dance = models.CharField(max_length=255)
    level_of_interest = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'

class MemberEntry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    class_year = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'