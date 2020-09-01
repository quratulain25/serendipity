from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=10)


class Task(models.Model):
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
