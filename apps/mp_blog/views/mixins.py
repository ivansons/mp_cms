"""Views mixins for mp_blog views"""
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from zinnia.search import QUERY


class EntryPreviewMixin(object):
    """
    Mixin implementing the preview of Entries requiring proper permissions
    from user.

    `permissions_required` is a list of permissions required to view entry.
    permissions_required = [
        'mp_blog.can_view_all_models',
    ]
    """

    permissions_required = []

    def get_queryset(self):
        """
        Return a queryset of with related fields.
        """
        return self.queryset().select_related(
            'image'
        ).prefetch_related(
            'authors',
            'categories',
        )

    def get_object(self, queryset=None):
        """
        If the status of the entry is not PUBLISHED,
        a preview is requested, so we check if the user
        has the 'can_view_all' permission or if it's an
        author of the entry.
        """
        qs = queryset or self.get_queryset()
        obj = get_object_or_404(qs, slug=self.kwargs.get('slug', ''))

        if obj.is_visible:
            return obj

        if self.request.user not in [author for author in obj.authors.all()]:
            for permission in self.permissions_required:
                if not self.request.user.has_perm(permission):
                    raise Http404(_('No entry found matching the query'))

        return obj


class NoCategoryEntryPreviewMixin(EntryPreviewMixin):
    def get_queryset(self):
        return self.queryset()


class EntrySearchMixin(object):
    """
    Mixin providing the behavior of the entry search view,
    by returning in the context the pattern searched, the
    error if something wrong has happened and finally the
    the queryset of published entries matching the pattern.
    """
    model_cls = None

    pattern = ''
    error = None

    def get_queryset(self):
        """
        Overridde the get_queryset method to
        do some validations and build the search queryset.
        """
        entries = self.model_cls.published.none()

        if self.request.GET:
            self.pattern = self.request.GET.get('q', '')
            if len(self.pattern) < 3:
                self.error = _('The pattern is too short')
            else:
                query_parsed = QUERY.parseString(self.pattern)
                entries = self.model_cls.published.filter(
                    query_parsed[0]).distinct()
                if not entries:
                    self.error = _("No entries found with %s pattern" % self.pattern)
        else:
            self.error = _('No pattern to search found')

        return entries

    def get_context_data(self, **kwargs):
        """
        Add error and pattern in context.
        """
        context = super(EntrySearchMixin, self).get_context_data(**kwargs)
        context.update({'error': self.error, 'pattern': self.pattern})
        return context
