from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    # 也可以用image = models.ImageField(upload_to='yes')
    url = models.URLField(blank=True)


# 讓project標題直接出現在管理介面中

    def __str__(self):
        return self.title
