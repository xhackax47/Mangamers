from django.contrib import admin

# Register your models here.
from django.utils.text import Truncator

from Mangamers.models import Manga, Anime, VideoGame, CategoryVideoGame, CategoryAnime, CategoryManga


class MangaAdmin(admin.ModelAdmin):
    # Configuration de la liste d'articles
    list_display = ('title', 'img', 'slug', 'category', 'author', 'release_date')
    prepopulated_fields = {'slug': ('title',), }
    list_filter = ('author', 'category',)
    date_hierarchy = 'release_date'
    ordering = ('release_date',)
    search_fields = ('title', 'content')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', ],
            'fields': ('title', 'img', 'slug', 'author', 'category', 'release_date')
        }),
        # Fieldset 2 : contenu du manga
        ('Description du manga', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('content',)
        }),
    )

    def preview_content(self, manga):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(manga.content).chars(40, truncate='...')

    # En-tête de notre colonne
    preview_content.short_description = 'Aperçu du contenu'


admin.site.register(Manga, MangaAdmin)
admin.site.register(CategoryManga)


class AnimeAdmin(admin.ModelAdmin):
    # Configuration de la liste d'articles
    list_display = ('title', 'img',  'slug', 'category', 'realisator', 'release_date')
    prepopulated_fields = {'slug': ('title',), }
    list_filter = ('realisator', 'category',)
    date_hierarchy = 'release_date'
    ordering = ('release_date',)
    search_fields = ('title', 'content')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', ],
            'fields': ('title',  'img', 'slug', 'realisator', 'category', 'release_date')
        }),
        # Fieldset 2 : contenu de l'article
        ('Description de l\'anime', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('content',)
        }),
    )

    def preview_content(self, anime):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(anime.content).chars(40, truncate='...')

    # En-tête de notre colonne
    preview_content.short_description = 'Aperçu du contenu'


admin.site.register(Anime, AnimeAdmin)
admin.site.register(CategoryAnime)


class VideoGameAdmin(admin.ModelAdmin):
    # Configuration de la liste d'articles
    list_display = ('title',  'img', 'slug', 'category', 'creator', 'platform', 'release_date')
    prepopulated_fields = {'slug': ('title',), }
    list_filter = ('creator', 'category',)
    date_hierarchy = 'release_date'
    ordering = ('release_date',)
    search_fields = ('title', 'content')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', ],
            'fields': ('title',  'img', 'slug', 'creator', 'category', 'platform', 'release_date')
        }),
        # Fieldset 2 : contenu de l'article
        ('Description du jeu vidéo', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('content',)
        }),
    )

    def preview_content(self, videogame):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(videogame.content).chars(40, truncate='...')

    # En-tête de notre colonne
    preview_content.short_description = 'Aperçu du contenu'


admin.site.register(VideoGame, VideoGameAdmin)
admin.site.register(CategoryVideoGame)
