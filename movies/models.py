from django.db import models
from django.utils import timezone
from PIL import Image


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    upload_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    watch_link = models.URLField(max_length=255)
    release_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.upload_image:
            super().save(*args, **kwargs)
            img = Image.open(self.upload_image.path)
            if img.height > 512 or img.width > 512:
                output_size = (512, 512)
                img.resize(output_size)
                img.save(self.upload_image.path)
