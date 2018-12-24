from django import forms
from identification_app.models import Profile
from main_app.models import Video, Playlist
from comments_app.models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)
		widgets = {
            'text': forms.TextInput(attrs={
                'id': 'textForm', 
                'required': True, 
                'placeholder': 'Say something...'
                })
            }


