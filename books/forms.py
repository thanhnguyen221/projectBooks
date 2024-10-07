from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DangKyForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email của bạn'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Nhập lại mật khẩu'}),
        }

class DangNhapForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Tên đăng nhập'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'})
    )
