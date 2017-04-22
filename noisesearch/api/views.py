from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PrivateSingleSerializer, PublicSingleSerializer
from noisesearch.handleUploadedFile import save_private_data, save_public_data


class PrivateSingle(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        serializer = PrivateSingleSerializer(data=request.data)

        print('user: ', request.user)

        if serializer.is_valid():
            serializer.save()
            # TODO: get data from file and add to the database
            file_path = settings.MEDIA_ROOT + serializer.data['file'][6:]

            save_private_data(file_path, str(request.user))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicSingle(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = PublicSingleSerializer(data=request.data)

        print('user: ', request.user.id)

        if serializer.is_valid():
            serializer.save()
            file_path = settings.MEDIA_ROOT + serializer.data['file'][6:]

            if request.user.id == None:
                username = 'Anonymous'
            else:
                username = str(request.user)

            save_public_data(file_path, username)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
