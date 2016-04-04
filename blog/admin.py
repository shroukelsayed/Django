from django.contrib import admin
from .models import Articles,Comments,Tags,Banwords,Emotions,System,UserProfile
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



class ApprovedListFilter(admin.SimpleListFilter):

    title = _('Is Approved')

    parameter_name = 'approved'

    def lookups(self, request, model_admin):
        return (
            ('is_approved', _('Approved')),
            ('not_approved', _('Not Approved')),
        )

    def queryset(self, request, queryset):
        
        if self.value() == 'approved':
            return queryset.filter(article_isApproved=True)
        if self.value() == 'not_approved':
            return queryset.filter(article_isApproved=False)

class PublishedListFilter(admin.SimpleListFilter):

    title= _('Is Published')

    parameter_name='published'

    def lookups(self, request, model_admin):
        return(
            ('published', _('Published')),
            ('not_published', _('Not Published')),
        )

    def queryset(self, request, queryset):
        
        if self.value() == 'published':
            return queryset.filter(article_isPublished=True)
        if self.value() == 'not_published':
            return queryset.filter(article_isPublished=False)
        


class ArticlesAdmin(admin.ModelAdmin):

    list_filter = (ApprovedListFilter,PublishedListFilter)
    list_display =['article_title','article_creationDate']
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(article_isPublished=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    make_published.short_description = "Mark selected stories as published"

admin.site.register(Articles,ArticlesAdmin)

class ApprovedListFilter(admin.SimpleListFilter):
    
    title = _('Is Approved')

    
    parameter_name = 'approved'

    def lookups(self, request, model_admin):
        
        return (
            ('approved', _('Approved')),
            ('not_approved', _('Not Approved')),
        )

    def queryset(self, request, queryset):
        
       
        if self.value() == 'approved':
            return queryset.filter(comment_isApproved=True)
        if self.value() == 'not_approved':
            return queryset.filter(comment_isApproved=False)

class CommentsAdmin(admin.ModelAdmin):
    list_filter = (ApprovedListFilter,)

admin.site.register(Comments,CommentsAdmin)	
admin.site.register(Tags)
admin.site.register(Banwords)
admin.site.register(Emotions)
admin.site.register(System)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)