from django.http import HttpResponse
def saludo(request):    #mi primera vista
    return HttpResponse("Hola mundo")

