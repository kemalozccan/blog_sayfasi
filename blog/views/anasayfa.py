from django.shortcuts import render

def anasayfa(request):
    d = {
        'ad' : 'Anasayfa'
    }

    return render(request, 'pages/anasayfa.html', context=d)