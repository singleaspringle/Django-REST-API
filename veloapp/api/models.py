from django.db import models

# Create your models here.
class Artist(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'artist'

class Hit(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_url = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'hit'