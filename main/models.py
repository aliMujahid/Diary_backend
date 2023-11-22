from django.db import models
from django.template.defaultfilters import slugify


class Topic(models.Model):
    """Topics are used to organize the entries."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Entry(models.Model):
    """Entries are writtings on some topic"""

    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='entries')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.topic.name + self.created.strftime("%m/%d/%Y, %H:%M:%S")
