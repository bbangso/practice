from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='제목',
        help_text='제목은100자이내로작성하세요',
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '제목 입력',
            }
        )
    )

    content = forms.CharField(
        label="내용",
        help_text = '자유롭게',
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = ['title', 'content']
        # fields = '__all__'


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']