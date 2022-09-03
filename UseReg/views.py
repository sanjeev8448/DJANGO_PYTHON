import mailbox
from django.shortcuts import render

# Create your views here.

def RegisterPage(request):
    return render(request,"app/register.html")

