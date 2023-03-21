from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    text = models.CharField(max_length=400, blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self) -> str:
        return self.title