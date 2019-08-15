from django.contrib import admin
from booksys import models
from .models import Author,Readers,Publisher,Category,Book,Brorrow,Returnbook,Administrators,Loss,Overdue

# Register your models here.
class Authoradmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email')

class Readersadmin(admin.ModelAdmin):
    list_display=('name', 'rid', 'sex', 'Contact_number')

class Publisheradmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'country', 'website')

class Bookadmin(admin.ModelAdmin):
    list_display=('bid', 'bname', 'publisher', 'publisher_date', 'publisher_state')
    search_fields=('bname',)
    list_filter=('publisher','publisher_date',)
    list_per_page=5
    list_editable=('bname','publisher_state',)
    list_select_related=('publisher',)
    filter_horizontal=('authors',)
    raw_id_fields=('publisher',)
    actions=['set_publisher_checkout','set_publisher_dai','set_publisher_status','set_publisher_del',]

    def set_publisher_checkout(modeladmin,request,queryset):
        selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='checkout')

    def set_publisher_dai(modeladmin,request,queryset):
        selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='dai')
    def set_publisher_status(modeladmin,request,queryset):
        selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).update(publisher_state='status')
    def set_publisher_del(modeladmin,request,queryset):
        selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        models.Book.objects.filter(id__in=selected).delete()

    set_publisher_checkout.short_description ="设置所有的书籍为--已出版"
    set_publisher_status.short_description="设置所有的书籍为--审核中"
    set_publisher_dai.short_description="设置所有的书籍为--待出版"
    set_publisher_del.short_description="设置所有的书籍为--删除"

class Brorrowadmin(admin.ModelAdmin):
    list_display = ('bookname', 'name', 'borrow_date')

class Returnbookadmin(admin.ModelAdmin):
    list_display = ('tname', 'Damage_situation', 'Expired_condition')

class Administratorsadmin(admin.ModelAdmin):
    list_display = ('name', 'aid')

class Categoryadmin(admin.ModelAdmin):
    list_display = ('name', 'cid')

class Lossadmin(admin.ModelAdmin):
    list_display = ('lname', 'penalty_money')

class Overdueadmin(admin.ModelAdmin):
    list_display = ('reader_id', 'penalty_money', 'overdue_date')

admin.site.register(models.Readers,Readersadmin)
admin.site.register(models.Author,Authoradmin)
admin.site.register(models.Publisher,Publisheradmin)
admin.site.register(models.Book,Bookadmin)
admin.site.register(models.Brorrow,Brorrowadmin)
admin.site.register(models.Returnbook,Returnbookadmin)
admin.site.register(models.Administrators,Administratorsadmin)
admin.site.register(models.Category,Categoryadmin)
admin.site.register(models.Loss,Lossadmin)
admin.site.register(models.Overdue,Overdueadmin)
# admin.site.register(Readers)
# admin.site.register(Author)
# admin.site.register(Publisher)
# admin.site.register(Book)
# admin.site.register(Brorrow)
# admin.site.register(Returnbook)
# admin.site.register(Administrators)
# admin.site.register(Category)
# admin.site.register(Loss)
# admin.site.register(Overdue)
# admin.site.register(Author,Readers)
# admin.site.register(Publisher,Category)
# admin.site.register(Book,Brorrow)
# admin.site.register(Returnbook,Administrators)
# admin.site.register(Loss,Overdue)
