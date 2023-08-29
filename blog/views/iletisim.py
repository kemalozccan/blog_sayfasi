from django.shortcuts import render
# from django.http import HttpResponse

def iletisim(request):
    context = {
        'sayi' : 5
    }
    return render(request, 'pages/iletisim.html', context=context)