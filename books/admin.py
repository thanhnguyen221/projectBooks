from django.contrib import admin
from .models import Sach, Chuong 

class ChuongInline(admin.TabularInline):
    model = Chuong
    extra = 1

class SachAdmin(admin.ModelAdmin):
    list_display = ('ten_sach', 'tac_gia', 'ngay_xuat_ban', 'the_loai') 
    search_fields = ('ten_sach', 'tac_gia')
    list_filter = ('ngay_xuat_ban', 'the_loai')  # Thêm trường thể loại vào bộ lọc
    inlines = [ChuongInline]

class ChuongAdmin(admin.ModelAdmin):
    list_display = ('sach', 'ten_chuong')  
    list_filter = ('sach',)

admin.site.register(Sach, SachAdmin)
admin.site.register(Chuong, ChuongAdmin)
