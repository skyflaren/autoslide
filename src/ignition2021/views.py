from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .presentation_creator import PresentationCreator
from zipfile import ZipFile
from .util import *
from wsgiref.util import FileWrapper
import os
import time
import shutil

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def home(request):
    return render(request,"home.html", {})

class FileView(APIView):
    def post(self, request, format=None):
        prs = request.data.get('file')
        filename = prs.name
        strippedname = filename.replace('.pptx', '')
        foldername = f"{strippedname.title()} Slides"

        path = default_storage.save('ppts/'+filename, ContentFile(prs.read()))
        print(path)
        
        # print("ONEEEEEEEEEE")
        prs_w = PresentationCreator(filename, foldername)
        # print("TWOOOOOOOOOO")
        prs_w.ReadPresentation()
        # print("THREEEEEEEEE")
        prs_w.Process()

        # Zip Folder
        zip_name = f"{foldername}.zip"

        file_paths = get_all_paths(f'./ppts/{foldername}')

        print('Following files will be zipped:')
        for file_name in file_paths:
            print(file_name)

        with ZipFile(zip_name,'w') as zip:
            for file in file_paths:
                zip.write(file)

        print(os.getcwd())
        zip_file = open(zip_name, 'rb+')
        print(zip_file)
        response = HttpResponse(FileWrapper(zip_file), content_type='application/zip', status=status.HTTP_200_OK)
        response['Content-Disposition'] = 'attachment; filename=%s'%zip_name
        
        return response

@api_view(('GET',))
def delete_view(request):
    if request.method == "GET":
        print("Clearing")
        now = time.time()
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "ppts")

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        return Response({}, status=status.HTTP_200_OK)