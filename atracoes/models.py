from django.db import models


class Atracao (models.Model):
    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"

    foto = models.ImageField(verbose_name="Foto", upload_to="atracoes")
    name = models.CharField(max_length=30, verbose_name="Nome")
    profissao = models.CharField(max_length=30, verbose_name= "Profissão")
    bio = models.TextField(verbose_name="Biografia", help_text="Uma breve descrição sobre a atração.")
    site = models.URLField(verbose_name="Site", help_text="https://instagram.com/")

    def __str__(self):
        return "%s - %s" % (self.name, self.profissao)

