from django.http import HttpResponse
def handler404(request, exception):
          return HttpResponse("<h1 style = 'color : red'>Dear User, The page you are looking for does not exists.</h1>", status = 404)