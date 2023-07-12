from django.contrib import admin
from .models import Question, Choice 

### for new sentence
# from .models import add_new

admin.site.register(Question)
admin.site.register(Choice)

## for new choice
# admin.site.register(new_choice)
