from django.db import models

from ProjectMangamers.settings import MEDIA_ROOT


class CategoryManga(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom")

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")
    img = models.ImageField(upload_to=MEDIA_ROOT, null=True)
    slug = models.SlugField(max_length=100, null=True)
    author = models.CharField(max_length=255, default="AUTHOR", verbose_name="Auteur")
    category = models.ForeignKey('CategoryManga', on_delete=models.CASCADE, null=True, verbose_name="Catégorie")
    content = models.TextField(null=False, verbose_name="Contenu")
    release_date = models.DateTimeField(verbose_name="Date de parution (XX/XX/XXXX)")

    class Meta:
        verbose_name = "Manga"
        verbose_name_plural = "Mangas"

    def __str__(self):
        return self.title


class CategoryAnime(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom")

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")
    img = models.ImageField(upload_to=MEDIA_ROOT, null=True)
    slug = models.SlugField(max_length=100, null=True)
    realisator = models.CharField(max_length=255, default="REALISATOR", verbose_name="Réalisateur")
    category = models.ForeignKey('CategoryAnime', on_delete=models.CASCADE, null=True, verbose_name="Catégorie")
    content = models.TextField(null=False, verbose_name="Contenu")
    release_date = models.DateTimeField(verbose_name="Date de sortie (XX/XX/XXXX)")

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animes"

    def __str__(self):
        return self.title


class CategoryVideoGame(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom")

    def __str__(self):
        return self.name


class VideoGame(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")
    img = models.ImageField(upload_to=MEDIA_ROOT, null=True)
    slug = models.SlugField(max_length=100, null=True)
    category = models.ForeignKey('CategoryVideoGame', on_delete=models.CASCADE, null=True, verbose_name="Catégorie")
    creator = models.CharField(max_length=200, default="CREATOR", verbose_name="Créateur")
    platform = models.CharField(max_length=100, verbose_name="Plateforme", null=True)
    content = models.TextField(null=False, verbose_name="Contenu")
    release_date = models.DateTimeField(verbose_name="Date de sortie (XX/XX/XXXX)")

    class Meta:
        verbose_name = "Jeu vidéo"
        verbose_name_plural = "Jeux vidéos"

    def __str__(self):
        return self.title