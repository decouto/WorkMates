from django.contrib import admin
from UserProject.models import UserProject, ProjectPage

class PageInline(admin.StackedInline):
	model = ProjectPage
	extra = 0

class UserProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields':['project_name']}),
		('Date', {'fields':['pub_date'], 'classes':['collapse']}),
		('Creator',{'fields':['creator']}),
	]
	inlines = [PageInline]

admin.site.register(UserProject, UserProjectAdmin)
