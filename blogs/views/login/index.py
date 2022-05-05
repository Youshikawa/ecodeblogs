from django.shortcuts import render
def index(request):
    return render(request, 'templates/login/login.html')