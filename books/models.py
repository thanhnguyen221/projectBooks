from django.db import models

class Sach(models.Model):
    ten_sach = models.CharField(max_length=200)
    tac_gia = models.CharField(max_length=200)
    ngay_xuat_ban = models.DateField()
    anh_bia = models.ImageField(upload_to='images/', null=True, blank=True)
    the_loai = models.CharField(max_length=100, blank=True, null=True)  # Thêm trường thể loại

    def __str__(self):
        return self.ten_sach

class Chuong(models.Model):
    sach = models.ForeignKey(Sach, related_name='chuong', on_delete=models.CASCADE)
    ten_chuong = models.CharField(max_length=200)
    noi_dung = models.TextField()

    def __str__(self):
        return f"{self.sach.ten_sach} - {self.ten_chuong}"
