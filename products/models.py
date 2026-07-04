from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to='products/')
    description = models.TextField()

    is_available = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    weight = models.CharField(max_length=50, blank=True)
    origin = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name