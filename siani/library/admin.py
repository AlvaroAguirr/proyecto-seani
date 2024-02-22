#AQUI se acutaliza la vista en el  menu admin de la base de datos 

from django.contrib import admin

from .models import Question, Module

class QuestionInline(admin.StackedInline):
    model = Question 
    extra = 3

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display =['name','description','num_questions']
    inlines =[QuestionInline
              ]
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['pk','question_text','module','right']
    list_filter =['module']