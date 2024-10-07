from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Sach, Chuong
from .form import SachForm, ChuongForm
from .utils import send_notification_email
from django.contrib.auth.decorators import login_required
from .forms import DangKyForm, DangNhapForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .utils import send_registration_email


def dang_ky(request):
    if request.method == 'POST':
        form = DangKyForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_email = form.cleaned_data.get('email')  # Email của người dùng
            username = form.cleaned_data.get('username')
            
            # Gửi email thông báo đăng ký thành công đến email của bạn
            send_registration_email(user_email, username)
            
            messages.success(request, 'Đăng ký thành công! Bạn có thể đăng nhập ngay bây giờ.')
            return redirect('dang_nhap')
        else:
            messages.error(request, 'Có lỗi xảy ra trong quá trình đăng ký. Vui lòng thử lại.')
    else:
        form = DangKyForm()
    return render(request, 'users/dang_ky.html', {'form': form})



def dang_nhap(request):
    if request.method == 'POST':
        form = DangNhapForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('danh_sach_sach')
            else:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác.')
    else:
        form = DangNhapForm()
    return render(request, 'users/dang_nhap.html', {'form': form})

def dang_xuat(request):
    logout(request)
    messages.success(request, 'Bạn đã đăng xuất thành công.')
    return redirect('dang_nhap')

@login_required
def danh_sach_sach(request):
    # Lấy dữ liệu từ cơ sở dữ liệu
    sach_list = Sach.objects.all()
    
    # Lấy giá trị tìm kiếm từ yêu cầu
    search_query = request.GET.get('q', '').lower()
    
    # Lọc sách theo từ khóa nếu có
    if search_query:
        sach_list = sach_list.filter(ten_sach__icontains=search_query)

    # Lấy giá trị thể loại từ yêu cầu
    selected_genre = request.GET.get('the_loai', '').lower()
    
    # Lọc sách theo thể loại nếu có
    if selected_genre:
        sach_list = sach_list.filter(the_loai__icontains=selected_genre)

    # Lấy danh sách các thể loại sách duy nhất
    unique_genres = Sach.objects.values_list('the_loai', flat=True).distinct()
    
    # Tạo ngữ cảnh để truyền dữ liệu vào template
    context = {
        'sach_list': sach_list,
        'unique_genres': unique_genres,
        'selected_genre': selected_genre,
        'search_query': search_query
    }
    return render(request, 'books/danh_sach_sach.html', context)
@login_required
def chi_tiet_sach(request, sach_id):
    # Lấy sách cụ thể hoặc trả về 404 nếu không tìm thấy
    sach = get_object_or_404(Sach, pk=sach_id)
    return render(request, 'books/chi_tiet_sach.html', {'sach': sach})

def them_sach_va_chuong(request):
    # Tạo formset cho chương với số lượng form bổ sung là 1
    ChuongFormSet = modelformset_factory(Chuong, form=ChuongForm, extra=1)

    if request.method == 'POST':
        sach_form = SachForm(request.POST, request.FILES)
        chuong_formset = ChuongFormSet(request.POST, queryset=Chuong.objects.none())  # Formset với queryset trống

        if sach_form.is_valid() and chuong_formset.is_valid():
            # Lưu sách trước
            sach_moi = sach_form.save()

            # Lưu từng chương trong formset
            for form in chuong_formset:
                chuong_moi = form.save(commit=False)
                chuong_moi.sach = sach_moi  # Gán sách mới vào chương
                chuong_moi.save()
                

            # Gửi email thông báo
            subject = 'Thông báo: Sách và chương mới được thêm'
            message = f'Sách "{sach_moi.ten_sach}" đã được thêm thành công cùng với các chương mới vào hệ thống.'
            recipient_list = ['thanhfff55@gmail.com']
            send_notification_email(subject, message, recipient_list)

            messages.success(request, 'Sách và các chương đã được thêm thành công!')
            return redirect('danh_sach_sach')
        else:
            messages.error(request, 'Form thêm sách hoặc formset chương không hợp lệ.')
    else:
        sach_form = SachForm()
        chuong_formset = ChuongFormSet(queryset=Chuong.objects.none())  # Hiển thị formset rỗng

    context = {
        'sach_form': sach_form,
        'chuong_formset': chuong_formset,
    }
    return render(request, 'books/them_sach_va_chuong.html', context)