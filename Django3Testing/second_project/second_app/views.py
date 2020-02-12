from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'index':"hello from second app"}

    return render(request,'second_app/index.html',context=my_dict)