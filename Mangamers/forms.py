from fileinput import FileInput

from django import forms
from django.forms import TextInput, DateInput, FileInput, DateTimeInput, Textarea
from django.forms.utils import ErrorList
from django.forms.widgets import ChoiceWidget

from Mangamers.models import Anime, Manga, VideoGame

class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])


class ContactForm(forms.Form):
    subject = forms.CharField(label="Sujet", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                              required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    sender = forms.EmailField(label="Votre adresse e-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}),
                              required=True)
    forwarding = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.",
                                    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        exclude = ['slug']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'img': FileInput(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
            'category': ChoiceWidget(attrs={'class': 'form-control'}).allow_multiple_selected,
            'content': Textarea(attrs={'class': 'form-control'}),
            'release_date': DateTimeInput(attrs={'class': 'form-control'}),
        }


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        exclude = ['slug']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'img': FileInput(attrs={'class': 'form-control'}),
            'realisator': TextInput(attrs={'class': 'form-control'}),
            'category': ChoiceWidget(attrs={'class': 'form-control'}).allow_multiple_selected,
            'content': Textarea(attrs={'class': 'form-control'}),
            'release_date': DateTimeInput(attrs={'class': 'form-control'}),
        }


class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        exclude = ['slug']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'img': FileInput(attrs={'class': 'form-control'}),
            'creator': TextInput(attrs={'class': 'form-control'}),
            'category': ChoiceWidget(attrs={'class': 'form-control'}).allow_multiple_selected,
            'platform': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'release_date': DateTimeInput(attrs={'class': 'form-control'}),
        }
