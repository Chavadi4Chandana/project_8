from django.shortcuts import render

# Create your views here.
def friendu(request):
    d={'name':'chandu'}
    return render(request,'friendu.html',d)
