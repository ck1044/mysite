# ---------------------------------------- [edit] ---------------------------------------- #
from django.http import HttpResponse
from django.shortcuts import render

from .models import Qusetion


def index(request):
    """
    pybo 목록 출력
    """

    question_list = Qusetion.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

# ---------------------------------------- [edit] ---------------------------------------- #
# Create your views here.
