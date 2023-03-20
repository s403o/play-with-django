from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify # to transform tittle

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null=False)
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                             null=False, db_index=True)  # book name 1 => book-name-1

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
    
    # def save(self, *args, **kwargs): # we called super because we want ovveide the built in save
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
