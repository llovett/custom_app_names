from django.db import models

class Foo(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()

class Bar(models.Model):
    age = models.IntegerField()


