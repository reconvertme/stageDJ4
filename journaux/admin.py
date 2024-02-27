from django.contrib import admin

# Register your models here.
from .models import Journal
# admin.site.register(Journal)

class JournalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'year_created')
admin.site.register(Journal, JournalAdmin)

from .models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur')
admin.site.register(Article, ArticleAdmin)