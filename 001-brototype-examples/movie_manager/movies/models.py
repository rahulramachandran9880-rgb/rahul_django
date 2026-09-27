from django.db import models

# Create your models here.

class CensorInfo(models.Model):
    rating = models.CharField(max_length=10)
    cirtified_by = models.CharField(max_length=100)

    def __str__(self):
        return self.cirtified_by

class Actor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
            return self.name

class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='images/', null=True,blank=True)
    censor_details = models.OneToOneField(CensorInfo, on_delete=models.SET_NULL, null=True, blank=True,related_name='movie')
    directed_by= models.ForeignKey('Director', on_delete=models.CASCADE,null=True, blank=True,
                                   related_name='directed_movies')

    directed_by= models.ForeignKey('Director', on_delete=models.CASCADE,null=True, blank=True,
                                       related_name='directed_movies')
    actors = models.ManyToManyField('Actor', related_name='acted_movies')

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name