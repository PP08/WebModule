from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PrivateSingleSerializer, PublicSingleSerializer, PrivateMultipleSerializer, PublicMultipleSerializer
from noisesearch.handleUploadedFile import save_private_data_single, save_public_data_single, save_private_data_multiple, save_public_data_multiple

from django.views.decorators.csrf import csrf_exempt


class PrivateSingle(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        serializer = PrivateSingleSerializer(data=request.data)

        print('user: ', request.user)

        if serializer.is_valid():
            serializer.save()
            # TODO: get data from file and add to the database
            file_path = settings.MEDIA_ROOT + serializer.data['file'][6:]


            # print(file_path)

            save_private_data_single(file_path, str(request.user))

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
                username = '*Anonymous user*'
            else:
                username = str(request.user)

            save_public_data_single(file_path, username)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrivateMultiple(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        serializer = PrivateMultipleSerializer(data=request.data)

        print('user: ', request.user)

        if serializer.is_valid():
            serializer.save()
            # TODO: get data from file and add to the database
            file_path = settings.MEDIA_ROOT + serializer.data['file'][6:]

            save_private_data_multiple(file_path, str(request.user))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicMultiple(APIView):
    """"""
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = PublicMultipleSerializer(data=request.data)

        # print('user: ', request.user.id)

        if serializer.is_valid():
            serializer.save()
            file_path = settings.MEDIA_ROOT + serializer.data['file'][6:]

            if request.user.id == None:
                username = '*Anonymous user*'
            else:
                username = str(request.user)

            save_public_data_multiple(file_path, username)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)