from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
    # 因此這一行代碼將所有內容從數據庫中獲取，將它們轉換為Python對象，然後將它們放在列表中。
