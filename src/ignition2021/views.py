from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .presentation_creator import PresentationCreator
from zipfile import ZipFile
from .util import *
from wsgiref.util import FileWrapper

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
        
        prs_w = PresentationCreator(filename, foldername)
        prs_w.ReadPresentation()
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

        response = FileResponse(open(zip_name, 'rb'), status=status.HTTP_200_OK)
        # response = FileResponse(zip_file, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={zip_name}'
        # response['Content-Length'] = temp.tell()
        # temp.seek(0)

        return response