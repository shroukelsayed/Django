from django.contrib import admin
from .models import Articles,Comments,Tags,Banwords,Emotions,System
from django.utils.translation import ugettext_lazy as _

class ApprovedListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Is Approved')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'approved'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('approved', _('Approved')),
            ('not_approved', _('Not Approved')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'approved':
            return queryset.filter(article_isApproved=True)
        if self.value() == 'not_approved':
            return queryset.filter(article_isApproved=False)

class ArticlesAdmin(admin.ModelAdmin):
    list_filter = (ApprovedListFilter,)

admin.site.register(Articles,ArticlesAdmin)

class ApprovedListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Is Approved')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'approved'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('approved', _('Approved')),
            ('not_approved', _('Not Approved')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
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
