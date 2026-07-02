from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def download_resume(request):
    return redirect(
        "https://drive.google.com/file/d/165FpdgUpg-k8iJQzMbubir-ENeKUG1nO/view?usp=sharing"
    )