from django.shortcuts import render

# Create your views here.

def previsao(request):
    return render(request, 'site_previsao/previsao.html')
