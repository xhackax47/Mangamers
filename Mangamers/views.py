from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from Mangamers.forms import ContactForm, MangaForm, AnimeForm, VideoGameForm, ParagraphErrorList
from Mangamers.models import Manga, Anime, VideoGame


def home(request):
    mangas = Manga.objects.all()
    animes = Anime.objects.all()
    videogames = VideoGame.objects.all()
    return render(request, 'Mangamers/index.html', locals())


def mangas(request):
    """ Afficher tous les mangas de notre site """
    mangas = Manga.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'Mangamers/mangas.html', {'all_mangas': mangas})


def manga_info(request, id, slug):
    """ Afficher un article complet """
    manga = get_object_or_404(Manga, id=id, slug=slug)
    return render(request, 'Mangamers/manga-info.html', {'manga': manga})


def new_manga(request):
    """ Créer un nouvel objet manga"""
    save = False
    form = MangaForm(request.POST or None, request.FILES, error_class=ParagraphErrorList)
    if form.is_valid():
        manga = Manga()
        manga.title = form.cleaned_data['title']
        manga.img = form.cleaned_data['img']
        manga.slug = form.cleaned_data['slug']
        manga.author = form.cleaned_data['author']
        manga.category.name = form.cleaned_data['category.name']
        manga.content = form.cleaned_data['content']
        manga.release_date = form.cleaned_data['release_date']
        manga.save()
        save = True

    return render(request, 'Mangamers/new-manga.html', {
        'form': form,
        'save': save
    })


def animes(request):
    """ Afficher tous les animes de notre site """
    animes = Anime.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'Mangamers/animes.html', {'all_animes': animes})


def anime_info(request, id, slug):
    """ Afficher un article complet """
    anime = get_object_or_404(Anime, id=id, slug=slug)
    return render(request, 'Mangamers/anime-info.html', {'anime': anime})


def new_anime(request):
    """ Créer un nouvel objet anime"""
    save = False
    form = AnimeForm(request.POST or None, request.FILES, error_class=ParagraphErrorList)
    if form.is_valid():
        anime = Anime()
        anime.title = form.cleaned_data['title']
        anime.img = form.cleaned_data['img']
        anime.slug = form.cleaned_data['slug']
        anime.realisator = form.cleaned_data['realisator']
        anime.category.name = form.cleaned_data['category.name']
        anime.content = form.cleaned_data['content']
        anime.release_date = form.cleaned_data['release_date']
        anime.save()
        save = True

    return render(request, 'Mangamers/new-anime.html', {
        'form': form,
        'save': save
    })


def videogames(request):
    """ Afficher tous les jeux vidéos de notre site """
    videogames = VideoGame.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'Mangamers/videogames.html', {'all_videogames': videogames})


def videogame_info(request, id, slug):
    """ Afficher un article complet """
    videogame = get_object_or_404(VideoGame, id=id, slug=slug)
    return render(request, 'Mangamers/videogame-info.html', {'videogame': videogame})


def new_videogame(request):
    """ Créer un nouvel objet jeu vidéo"""
    save = False
    form = VideoGameForm(request.POST or None, request.FILES, error_class=ParagraphErrorList)
    if form.is_valid():
        videogame = VideoGame()
        videogame.title = form.cleaned_data['title']
        videogame.img = form.cleaned_data['img']
        videogame.slug = form.cleaned_data['slug']
        videogame.creator = form.cleaned_data['creator']
        videogame.platform = form.cleaned_data['platform']
        videogame.category.name = form.cleaned_data['category.name']
        videogame.content = form.cleaned_data['content']
        videogame.release_date = form.cleaned_data['release_date']
        videogame.save()
        save = True

    return render(request, 'Mangamers/new-videogame.html', {
        'form': form,
        'save': save
    })


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None, error_class=ParagraphErrorList)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        forwarding = form.cleaned_data['forwarding']
        sending = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'Mangamers/contact.html', locals())
