from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from quora.models import Answer,  Question

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'minlength': 8})
        self.fields['password2'].widget.attrs.update({'minlength': 8})

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if len(password2) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password2


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        
