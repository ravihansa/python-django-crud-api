from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    web_site = models.CharField(max_length=100)
    logo_path = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
