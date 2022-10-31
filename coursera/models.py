from django.db import models

# Create your models here.

class CourseraModel(models.Model):
    category = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = "categories"
