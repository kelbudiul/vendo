from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    pass

@login_required
def dashboard(request):
    pass
