from django.shortcuts import render

def post_track(request):
    return render(request, 'post-track.html')
