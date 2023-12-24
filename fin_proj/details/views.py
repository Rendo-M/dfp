from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    context = {'title':'Список чертежей', 'content':'вот ваш список сэр', 'acln':['АЦЛН.005001.000.00','АЦЛН.005001.001.00','АЦЛН.005001.002.00']}
    return render(request, 'details/index.html', context)

def number(request, specification):
    
    return HttpResponse(f"<h2>Перед вами новейшая разработка <br>{specification}</h2>")

def page404(request, exception):
    return HttpResponseNotFound('<center><h1>Страница<br> не найдена</h1>')
