from django.contrib import admin
from resume.models import contact
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


admin.site.register(contact, ContactUsAdmin)