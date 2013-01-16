from django.contrib import admin
from ForumQuestion.models import Question, Answer

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Question', {'fields': ['question']}),
		('Asker',{'fields':['asker']}),
		('Date', {'fields':['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
