from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms as django_forms

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']

        widgets = {
            'email': django_forms.TextInput(attrs={'placeholder': 'example@email.com'}),
            'name': django_forms.TextInput(attrs={'placeholder': 'Doe'}),
            'username': django_forms.TextInput(attrs={'placeholder': 'ID'}),
            'password' : django_forms.PasswordInput(attrs={'placeholder': 'password'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_apssword(self.cleaned_data['password'])
        if commit:
            user.save()
        return user