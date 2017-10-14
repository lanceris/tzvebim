from django.shortcuts import render, redirect
from django.contrib.auth.views import logout

import vk

def index(request):
    try:
        social = request.user.social_auth.get(provider='vk-oauth2')
        access_token = social.extra_data.get('access_token')
        session = vk.Session(access_token=access_token)
        api = vk.API(session)
        friends = api.friends.get(count=5, order='random', fields=['photo_50'])
    except:
        friends = {}
    return render(request, 'index.html', {'friends': friends})

def log_out(request):
    logout(request)
    return redirect('/')