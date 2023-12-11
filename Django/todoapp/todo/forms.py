from django import forms
from .models import Todo

# 생성 로직
# ModelForm 자동완성    
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','description','important')
