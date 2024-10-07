from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def trang_chinh(request):
    if request.user.is_authenticated:
        return redirect('danh_sach_sach')  # Hoặc trang mặc định khác
    else:
        return redirect('dang_ky')  # Hoặc trang đăng nhập
