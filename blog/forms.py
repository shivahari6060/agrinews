from .models import Comment, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields =('first_name', 'last_name', 'email', 'message')

	class ContactForm(object):
		"""docstring for ContactForm"""
		def __init__(self, arg):
			super(ContactForm, self).__init__()
			self.arg = arg
			
			