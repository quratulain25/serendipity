from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=32)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=32)
    is_complete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.title
