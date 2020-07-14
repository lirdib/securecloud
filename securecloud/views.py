
from django.shortcuts import render

def main(request):
    return render(request, 'base_loyout.html')