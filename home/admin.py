from django.contrib import admin
from .models import Employee, Role, Department
from .form import ItemForm
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    form = ItemForm

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.0.min.js',
            '/static/js/index.js',)

admin.site.register(Employee,ItemAdmin)
admin.site.register(Role)
admin.site.register(Department)
