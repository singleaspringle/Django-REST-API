from rest_framework import serializers
from .models import Artist, Hit

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class HitSerializer(serializers.ModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Hit
        fields = ['id', 'title', 'title_url', 'created_at', 'updated_at', 'artist_id']
        read_only_fields = ['created_at', 'updated_at', 'title_url']

    def create(self, validated_data):
        title = validated_data['title']
        validated_data['title_url'] = title.lower().replace(" ", "-")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title_url'] = validated_data['title'].lower().replace(" ", "-")
        return super().update(instance, validated_data)