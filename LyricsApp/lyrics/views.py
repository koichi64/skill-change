from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Artist, Song, Lyrics
from .forms import ArtistForm, SongForm, LyricsForm


class Index(ListView):
    template_name = 'index.html'
    model = Artist


class ArtistList(ListView):
    template_name = 'artist_list.html'
    model = Artist


class ArtistDetail(DetailView):
    template_name = 'artist_detail.html'
    model = Artist


class AddArtist(CreateView):
    template_name = 'add_artist.html'
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy('artist_list')


class UpdateArtist(UpdateView):
    template_name = 'update_artist.html'
    model = Artist
    form_class = ArtistForm

    def get_success_url(self):
        success_url = reverse_lazy('artist_detail', kwargs={'pk': self.kwargs['pk']})
        return success_url


class DeleteArtist(DeleteView):
    model = Artist
    success_url = reverse_lazy('artist_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SongDetail(DetailView):
    template_name = 'song_detail.html'
    model = Song


class AddSong(CreateView):
    template_name = 'add_song.html'
    model = Song
    form_class = SongForm

    def get_success_url(self):
        success_url = reverse_lazy('artist_detail', kwargs={'pk': self.kwargs['pk']})
        return success_url


class UpdateSong(UpdateArtist):
    template_name = 'update_song.html'
    model = Song
    form_class = SongForm

    def get_success_url(self):
        success_url = reverse_lazy('song_detail', kwargs={'pk': self.kwargs['pk']})
        return success_url


class DeleteSong(DeleteView):
    model = Song

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        success_url = reverse_lazy('artist_detail', kwargs={'pk': self.kwargs['artist_pk']})
        return success_url


class AddLyrics(CreateView):
    template_name = 'add_lyrics.html'
    model = Lyrics
    form_class = LyricsForm

    def get_success_url(self):
        success_url = reverse_lazy('song_detail', kwargs={'pk': self.kwargs['pk']})
        return success_url


class UpdateLyrics(UpdateView):
    template_name = 'update_lyrics.html'
    model = Lyrics
    form_class = LyricsForm

    def get_success_url(self):
        success_url = reverse_lazy('song_detail', kwargs={'pk': self.kwargs['song_pk']})
        return success_url


class DeleteLyrics(DeleteView):
    model = Lyrics

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        success_url = reverse_lazy('song_detail', kwargs={'pk': self.kwargs['song   _pk']})
        return success_url
