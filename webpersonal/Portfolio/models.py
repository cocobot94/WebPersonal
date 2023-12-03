from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    web = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name = 'projecto'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title





