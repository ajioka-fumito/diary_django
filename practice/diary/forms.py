from django import forms
from .models import Day,Comment

class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__'

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_id','comment')
        widgets = {
            'comment_id':forms.HiddenInput()
        } 