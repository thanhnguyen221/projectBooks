# forms.py
from django import forms
from .models import Sach, Chuong




class SachForm(forms.ModelForm):
    class Meta:
        model = Sach
        fields = ['ten_sach', 'tac_gia', 'ngay_xuat_ban', 'anh_bia', 'the_loai']
        widgets = {
            'ngay_xuat_ban': forms.DateInput(attrs={'type': 'date'}),
        }

class ChuongForm(forms.ModelForm):
    class Meta:
        model = Chuong
        fields = [ 'ten_chuong', 'noi_dung']
