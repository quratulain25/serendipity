from django.db import models


class Page(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, editable=True)


class Task(models.Model):
    def __str__(self):
        return self.page_id.title

    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, editable=True)
