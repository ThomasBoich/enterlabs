from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import CustomUser, Profile, MedCard


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'last_name', 'first_name', 'patronymic')

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError(
                _("Password must be at least 8 characters long.")
            )
        if password.isdigit():
            raise ValidationError(
                _("Password should contain at least one letter.")
            )
        if password.isalpha():
            raise ValidationError(
                _("Password should contain at least one digit.")
            )
        return password

    def get_password_recommendations(self):
        password = self.cleaned_data.get('password1')
        recommendations = []
        if len(password) < 12:
            recommendations.append(
                _("Use at least 12 characters.")
            )
        if not any(x.isupper() for x in password):
            recommendations.append(
                _("Include uppercase letters.")
            )
        if not any(x.islower() for x in password):
            recommendations.append(
                _("Include lowercase letters.")
            )
        if not any(x.isdigit() for x in password):
            recommendations.append(
                _("Include digits.")
            )
        return recommendations

      
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'pasport_series', 'pasport_number', 'phone', 'addres']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    error_messages = {
        "invalid_login": 
            'НЕВЕРНЫЙ ЛОГИН И/ИЛИ ПАРОЛЬ. Попробуйте снова.'
        ,
        "inactive": "This account is inactive.",
    }
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                "Этот аккаунт не активен.",
                code='inactive',
            )
        if user.ban:
            raise ValidationError(
                "Вы не можете войти, обратитесь к администратору",
                code='fired',
            )

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']


    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    patronymic = forms.CharField(label='Отчество', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pasport_series = forms.CharField(label='Серия паспорта', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pasport_number = forms.CharField(label='Номер паспорта', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    addres = forms.CharField(label='Адрес', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'pasport_series', 'pasport_number', 'phone', 'addres']
        exclude = ['username', 'sender']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # fields = [ 'adress', 'phone', 'pasport_series', 'pasport_number', 'photo',]

class MedCardUpdateForm(forms.ModelForm):
    height = forms.CharField(label='Рост', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.CharField(label='Вес', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    blood = forms.CharField(label='Группа Крови', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(label='Возраст', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MedCard
        # fields = '__all__'
        fields = ['height', 'weight', 'blood', 'age']



from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), label=_("Email"))

    class Meta:
        fields = ('email', 'password')