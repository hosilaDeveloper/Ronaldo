from django.db import models


class Service(models.Model):
    icon = models.ImageField(upload_to='icon')
    profession = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.profession


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class GetInTouch(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
