from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dang-ky/', views.dang_ky, name='dang_ky'),
    path('dang-nhap/', views.dang_nhap, name='dang_nhap'),
    path('dang-xuat/', LogoutView.as_view(), name='dang_xuat'),  # Sử dụng LogoutView của Django
    path('logout/', LogoutView.as_view(), name='logout'),  # Hoặc xóa nếu không cần
    path('', views.danh_sach_sach, name='danh_sach_sach'),
    path('sach/<int:sach_id>/', views.chi_tiet_sach, name='chi_tiet_sach'),
    path('them/', views.them_sach_va_chuong, name='them_sach_va_chuong'),
    
]
