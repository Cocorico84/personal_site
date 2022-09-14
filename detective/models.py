from django.db import models


class Suspect(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    job = models.CharField(max_length=16, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Weapon(models.Model):
    name = models.CharField(max_length=16)
    type = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name
