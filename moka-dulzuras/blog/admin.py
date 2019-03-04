from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """docstring for CategoryAdmin."""
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    """docstring for PostAdmin."""
    list_display = ('title', 'author', 'published','post_categories',)
    readonly_fields = ('created', 'updated')
    # Ordena primero por author y luego por fecha de publicacion
    orderin = ('author', 'published')
    search_fields = ('title','content','author__username', 'categories__name')
    # Las __ luego de author se usan para indicar el field dentro del modelo
    # de la relacion
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name',)

    def post_categories(self, obj):
        return ",".join(c.name for c in obj.categories.all().order_by('name'))

    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
