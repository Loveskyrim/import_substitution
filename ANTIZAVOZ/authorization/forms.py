from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=(forms.EmailInput()),
        max_length=64,
        required=True)

    is_organisation = forms.BooleanField(
        label='Как организация/компания',
        required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'is_organisation', 'password1', 'password2')

    # описание ошибок для каждого поля, синтаксис clean_<имя_поля>, 
    # для простой формы над полями - clean() // UI не особо красивый, поэтому не используется
    # для наглядности ошибки применяется message.error в views.py
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Эта почта уже зарегестрирована")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Пользователь уже зарегестрирован")
        return username
    
    # def clean_category(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise ValidationError("Пользователь уже зарегестрирован")
    #     return username

    def clean_passwd2(self):
        passwd1 = self.cleaned_data.get('password1')
        passwd2 = self.cleaned_data.get('password2')
        if passwd1 != passwd2:
            raise ValidationError("Пароли не совпадают")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user