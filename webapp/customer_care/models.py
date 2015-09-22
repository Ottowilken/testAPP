from django.db import models

__author__ = 'Otto'


class User(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField()
        password = models.CharField(max_length=50)
        password_confirm = models.CharField(max_length=50)


class Todo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField()

    def __unicode__(self):
        return self.name

