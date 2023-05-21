from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='sub_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)  # Slug alanını ekleyin

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Slug alanını otomatik olarak oluşturun
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
