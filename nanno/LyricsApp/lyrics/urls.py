from django.urls import path
from .views import ArtistList, ArtistDetail, SongDetail, \
    AddArtist, AddSong, AddLyrics, UpdateArtist, UpdateSong, UpdateLyrics, \
    DeleteArtist, DeleteSong, DeleteLyrics, Index

urlpatterns = [
    path('artist/', ArtistList.as_view(), name='artist_list'),
    path('artist/<int:pk>/', ArtistDetail.as_view(), name='artist_detail'),
    path('artist/add/', AddArtist.as_view(), name='add_artist'),
    path('artist/update/<int:pk>', UpdateArtist.as_view(), name='update_artist'),
    path('artist/delete/<int:pk>', DeleteArtist.as_view(), name='delete_artist'),
    path('song/<int:pk>/', SongDetail.as_view(), name='song_detail'),
    path('song/add/<int:pk>/', AddSong.as_view(), name='add_song'),
    path('song/update/<int:pk>/', UpdateSong.as_view(), name='update_song'),
    path('song/delete/<int:artist_pk>/<int:pk>/', DeleteSong.as_view(), name='delete_song'),
    path('lyrics/add/<int:pk>/', AddLyrics.as_view(), name='add_lyrics'),
    path('lyrics/update/<int:song_pk>/<int:pk>', UpdateLyrics.as_view(), name='update_lyrics'),
    path('lyrics/delete/<int:song_pk>/<int:pk>/', DeleteLyrics.as_view(), name='delete_lyrics'),
    path('', Index.as_view(), name='index'),
]
