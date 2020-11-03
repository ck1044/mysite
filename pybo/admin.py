# ---------------------------------------- [edit] ---------------------------------------- #
from django.contrib import admin

from .models import Qusetion, Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Qusetion, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
# ---------------------------------------------------------------------------------------- #
