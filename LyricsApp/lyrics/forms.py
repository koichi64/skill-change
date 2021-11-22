from django import forms
from .models import Artist, Song, Lyrics


class BootStrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ArtistForm(BootStrapForm):
    class Meta:
        model = Artist
        fields = ('name', 'image')


class SongForm(BootStrapForm):
    class Meta:
        model = Song
        fields = ('artist', 'name', 'image', 'category', 'movie_url')


class LyricsForm(BootStrapForm):
    class Meta:
        model = Lyrics
        fields = ('song', 'name', 'content', 'language')
