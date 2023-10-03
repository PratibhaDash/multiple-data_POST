from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer
from django.shortcuts import render




## in this class multiple file upload
class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        # Get a list of uploaded files
        files = request.FILES.getlist('image')

        # Validate and save each file
        data = []
        for file in files:
            serializer = MyModelSerializer(data={'name': request.data.get('name'), 'image': file})
            if serializer.is_valid():
                serializer.save()
                data.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data, status=status.HTTP_201_CREATED)

    # def upload_images(request):
    #     return render(request, 'upload.html')