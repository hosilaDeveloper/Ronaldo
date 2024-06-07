from django.db import models
from main.models import Category


class Partner(models.Model):
    image = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.image.name


class About(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='person')
    birth = models.DateField()
    live = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    projects = models.IntegerField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    type = models.CharField(max_length=221)
    is_skill = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.type:
            return self.type
        return 'Skill'


class AdditionalInfo(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    # experience
    start_finish = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    academy = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='icon', null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    # is skill
    title = models.CharField(max_length=221, null=True, blank=True)
    percent = models.IntegerField(null=True, blank=True)
    is_main = models.BooleanField(default=False)


class Projects(models.Model):
    image = models.ImageField(upload_to='projects')
    category = models.ManyToManyField(Category, blank=True)
    link = models.URLField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.profession

