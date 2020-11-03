# ---------------------------------------- [edit] ---------------------------------------- #
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Qusetion


def index(request):
    """
    pybo 목록 출력
    """

    question_list = Qusetion.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Qusetion, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

# ---------------------------------------- [edit] ---------------------------------------- #


# Create your views here.
