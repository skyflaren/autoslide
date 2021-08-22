from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def home(request):
    return render(request,"home.html", {})

class FileView(APIView):
    def post(self, request, format=None):
        try:
            prs = request.data.get('file')
            filename = prs.name

            path = default_storage.save('slides/'+filename, ContentFile(prs.read()))
            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({'Bad Request':'Error uploading file'}, status=status.HTTP_400_BAD_REQUEST)