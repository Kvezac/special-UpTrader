from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Menu title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Menu slug")
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name="children")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ["pk"]

    def __str__(self):
        return self.name

