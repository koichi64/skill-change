from django.db import models


# Create your models here.
class Artist(models.Model):
    class Meta:
        db_table = 'artist'

    name = models.CharField(verbose_name='アーティスト名', max_length=31)
    image = models.ImageField(verbose_name='画像', null=True, blank=True)

    def __str__(self):
        return self.name


SONG_CATEGORY = (('K-POP', 'K-POP'), ('J-POP', 'J-POP'), ('ELSE', 'その他'))


class Song(models.Model):
    class Meta:
        db_table = 'song'

    artist = models.ForeignKey(Artist, verbose_name='アーティスト', on_delete=models.CASCADE, related_name='song')
    name = models.CharField(verbose_name='曲名', max_length=31)
    category = models.CharField(max_length=31, choices=SONG_CATEGORY)
    image = models.ImageField(verbose_name='画像', null=True, blank=True)
    movie_url = models.URLField(verbose_name='動画URL', max_length=128, blank=True)

    def __str__(self):
        return self.artist.name + '/' + self.name


LYRICS_LAUGUAGE = (('Japanese', '日本語'), ('English', '英語'), ('Korean', '韓国語'), ('Chinese', '中国語'))


class Lyrics(models.Model):
    class Meta:
        db_table = 'lyrics'

    song = models.ForeignKey(Song, verbose_name='曲', on_delete=models.CASCADE, related_name='lyrics')
    name = models.CharField(verbose_name='タイトル', max_length=31)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    language = models.CharField(max_length=31, choices=LYRICS_LAUGUAGE)

    def __str__(self):
        return self.song.name + '/' + self.name
