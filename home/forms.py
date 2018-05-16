from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget



class RegistrationForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(attrs={'class':'validate'}), label="")
    name = forms.CharField(label = 'Họ và tên', max_length=50)
    username = forms.CharField(label = 'Tài khoản', max_length=30)
    email = forms.EmailField(label='email')
    address = forms.CharField(label='Địa chỉ', max_length=60)
    password = forms.CharField(label='Mật khẩu', widget = forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget = forms.PasswordInput())


    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password == password2 and password:
                return password2
            raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'],password=self.cleaned_data['password'] )
