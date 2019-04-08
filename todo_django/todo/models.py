from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(default = '', max_length = 300)
    image_url = models.CharField(default = '', max_length = 600)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(default = '', max_length = 200)
    image_url = models.CharField(default = '', max_length = 600)
    subject = models.CharField(default = '', max_length = 200)
    education = models.CharField(default = '', max_length = 200)
    school = models.ForeignKey(School, on_delete = 'CASCADE', related_name = 'professors')

    def __str__(self):
        return self.name