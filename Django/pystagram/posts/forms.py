from django import forms
from posts.models import Comment,Post

class CommentForm(forms.ModelForm):
    content= forms.CharField()
    class Meta:
        model = Comment
        fields = {
            "post",
            "content",
            
        }
        widegets = {
            "contents": forms.Textarea(
                attrs={
                    "placeholder":"댓글달기",
                }
            )
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
        ]