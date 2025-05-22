from django.core.management.base import BaseCommand
from api.models import Artist, Hit
from django.utils.timezone import now

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        artists = [
            Artist.objects.create(first_name='John', last_name='Doe'),
            Artist.objects.create(first_name='Jane', last_name='Smith'),
            Artist.objects.create(first_name='Alice', last_name='Cooper'),
        ]

        for i in range(20):
            Hit.objects.create(
                title=f'Song {i}',
                title_url=f'song-{i}',
                artist=artists[i % 3],
            )