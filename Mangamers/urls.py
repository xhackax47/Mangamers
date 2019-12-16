from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # Liens courants
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    url(r'^cgu$', TemplateView.as_view(template_name='Mangamers/cgu.html')),

    # Liens Manga
    path('mangas/', views.mangas, name='mangas'),
    path('mangas/<int:id>-<slug:slug>', views.manga_info, name='manga_info'),
    path('new-manga/', views.new_manga, name='new_manga'),

    # Liens Anime
    path('animes/', views.animes, name='animes'),
    path('animes/<int:id>-<slug:slug>', views.anime_info, name='anime_info'),
    path('new-anime/', views.new_anime, name='new_anime'),

    # Liens Jeu Vidéo
    path('videogames/', views.videogames, name='videogames'),
    path('videogames/<int:id>-<slug:slug>', views.videogame_info, name='videogame_info'),
    path('new-videogame/', views.new_videogame, name='new_videogame'),
]