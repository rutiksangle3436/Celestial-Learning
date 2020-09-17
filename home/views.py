from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'index.html')


def video_play(request):
    videos = [
        'baba',
        'coffine',
        'engineers',
        'rushikesh',
        'saumya',
    ]
    data = {'videos': videos}
    return render(request, 'video.html', data)