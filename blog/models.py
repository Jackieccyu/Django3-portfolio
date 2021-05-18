from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()


# 讓blog標題直接出現在管理介面中

    def __str__(self):
        return self.title
