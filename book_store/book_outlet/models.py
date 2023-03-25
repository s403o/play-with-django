from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify # to transform tittle

# Create your models here.

class Country(models.Model):
     name = models.CharField(max_length=80)
     code = models.CharField(max_length=2)

     def __str__(self):
        return f"{self.name} ({self.code})"
     class Meta: # used to add special options
        verbose_name_plural = "countries"
class Address(models.Model):
     street = models.CharField(max_length=80)
     postal_code = models.CharField(max_length=5)
     city = models.CharField(max_length=15)

     def __str__(self):
          return f"{self.street}, {self.postal_code}, {self.city}"
    
     class Meta: # used to add special options
        verbose_name_plural = "Adress"
        get_latest_by = "order_date"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) # one to one

    def full_name(self):
         return f"{self.first_name} {self.last_name}"

    def __str__(self):
            return self.full_name()
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # one to Many
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                             null=False, db_index=True)  # book name 1 => book-name-1
    published_countries = models.ManyToManyField(Country) # many to many
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
    
    # def save(self, *args, **kwargs): # we called super because we want ovveide the built in save
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
