from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {'latest_question_list': 'Hola'}
    return render(request, 'gs/index.html', context)
