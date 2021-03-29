from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(label='Add comment:', widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 15}))
