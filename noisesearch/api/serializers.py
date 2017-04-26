from rest_framework import serializers
from noisesearch.models import PrivateFilesSingle, PublicFilesSingle, PrivateFilesMultiple, PublicFilesMultiple


class PrivateSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFilesSingle
        fields = ('file', 'uploaded_at')


class PublicSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicFilesSingle
        fields = ('file', 'uploaded_at')


class PrivateMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFilesMultiple
        fields = ('file', 'uploaded_at')


class PublicMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicFilesMultiple
        fields = ('file', 'uploaded_at')
