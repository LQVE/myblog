from django.contrib import admin
from .models import *

# 2.定义Models的高级管理类展现形式

# aUser
class UserAdmin(admin.ModelAdmin):
    list_display = ("username","qq","last_login",)
    search_fields = ("username","qq",)
    list_filter = ("username",)
    exclude = ()
    date_hierarchy = "date_joined"

#Article
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        # ('高级设置', {
        #     'classes': ('collapse',),
        #     'fields': ('click_count', 'is_recommend',)
        # }),
    )

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

# Ad
class AdAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)
    fields = ("title","description","image_url",)
    date_hierarchy = "date_publish"

# Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    fields = ("name",)


# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    fields = ("name",)


# Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_fields = ("username",)
    fields = ("username","content","article",)

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )


# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Ad,AdAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)


#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(Publisher)
#
# class AuthorAdmin(admin.ModelAdmin):
#     #后台显示的字段
#     list_display = ("name","age","email")
#     #指定在列表页能够连接到详情页的字段
#     list_display_links = ("name", "email")
#     #指定在列表页中允许被修改的字段
#     list_editable = ("age",)
#     #指定允许被搜索的字段
#     search_fields = ("name","email",)
#     #在列表页的右侧增加一个过滤器，允许实现快速筛选
#     list_filter = ("name","email",)
#     #在列表页的顶部加一个时间选择器
#     # date_hierarchy = ()
#     #在详情页面上，要显示那些字段，并按照什么显示
#     #fields = ("name","age",)
#     #指定在详情页的字段分组,与fields有冲突
#     # fieldsets = (
#     #     #分组1
#     #     (
#     #         "基本选项", {
#     #             "fields": ("name", "age"),
#     #         }
#     #     ),
#     #     #分组2
#     #     (
#     #         "高级选项",{
#     #             "fields":("email","isactive"),
#     #             "classes":("collapse",)
#     #         }
#     #     ),
#     # )
#