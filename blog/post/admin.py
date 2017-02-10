from django.contrib import admin

from models import Post, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
	'''
	Tabular Inline View for Post
	'''
	model = Comment
	max_num = 10
	extra = 1

class PostAdmin(admin.ModelAdmin):
	'''
		Admin View for Post
	'''
	list_display = ('title', 'date_time', 'author', 'likes')
	list_filter = ('title', 'date_time', 'author')
	inlines = [
		CommentInline,
	]
	search_fields = ('title', 'content', 'date_time', 'author', 'likes')
	list_display_links = ('title', 'date_time', 'author', 'likes')


admin.site.register(Post, PostAdmin)
