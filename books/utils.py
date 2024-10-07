from django.core.mail import send_mail
from django.conf import settings
# utils.py


from django.core.mail import send_mail

def send_registration_email(user_email, username):
    subject = 'Có 1 tài khoản đăng ký thành công!'
    message = f'Tài khoản {username},\n\n Đã đăng ký thành công trên hệ thống !'
    from_email = settings.DEFAULT_FROM_EMAIL  # Sử dụng email mặc định từ settings.py
    recipient_list = [user_email]
     # Danh sách email nhận thông báo, bao gồm email của bạn
    recipient_list = ['thanhfff55@gmail.com']  # Thay 'your_email@gmail.com' bằng email của bạn
    
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,  # Đặt thành False để thấy lỗi nếu có
    )



def send_notification_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list
    )
