from django.shortcuts import render


def webmap(request):
    return render(request, 'map/webmap.html')
