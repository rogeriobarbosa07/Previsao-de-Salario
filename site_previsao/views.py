from django.shortcuts import render

# Create your views here.

def previsao(request):
    if request.method == 'POST':
        return # trocar

    return render(request, 'site_previsao/previsao.html')
