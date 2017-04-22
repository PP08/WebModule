from rest_framework import serializers
from noisesearch.models import PrivateFilesSingle, PublicFilesSingle


class PrivateSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFilesSingle
        fields = ('file', 'uploaded_at')


class PublicSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicFilesSingle
        fields = ('file', 'uploaded_at')
