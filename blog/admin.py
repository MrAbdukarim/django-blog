from django.contrib import admin
from .models import Post, About
from ckeditor.widgets import CKEditorWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    body_en = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'created_at')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'updated_at')


admin.site.register(Post, PostAdmin)
