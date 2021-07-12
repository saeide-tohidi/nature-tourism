from django.shortcuts import  HttpResponse

def index(request):
    return HttpResponse('<h1><a href=http://127.0.0.1:8006/swagger> go to API swagger doc </a></h1>')
