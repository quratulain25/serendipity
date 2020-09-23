from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=32)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    is_complete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.page_id.title
