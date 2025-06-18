from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    category = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.name} - {self.subject}"