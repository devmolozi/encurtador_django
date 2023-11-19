from django.db import models


class Link(models.Model):
    link_redirect = models.URLField()
    link_encurtado = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.link_encurtado
