from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ('titulo','categoria','publicado_flag','publicado')
    list_filter         = ('publicado_flag','categoria')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields       = ('titulo','extracto')
