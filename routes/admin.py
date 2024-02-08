from django.contrib import admin

from .models import Route

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     """
#     Админ-панель модели категорий
#     """

#     list_display = ('id', 'title', 'slug')
#     prepopulated_fields = {'slug' : ('title',)}

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    """Админ-панекль модели маршрутов"""

    list_display = ('id', 'name', 'complexity', 'price')
    prepopulated_fields = {'slug' : ('name', )}
    list_filter = ['complexity', 'price']