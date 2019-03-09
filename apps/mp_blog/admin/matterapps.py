from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from orderable.admin import OrderableAdmin

from zinnia.admin.entry import EntryAdmin
from zinnia.admin.filters import AuthorListFilter
from zinnia.managers import DRAFT, PUBLISHED
from zinnia.settings import PING_DIRECTORIES

from .forms import MatterAppsAdminForm

from ..models.matterapps import MatterAppsEntry

class MatterAppsEntryAdmin(OrderableAdmin, EntryAdmin):
    form = MatterAppsAdminForm
    date_hierarchy = 'creation_date'

    fieldsets = (
        (_('Resource'), {
            'fields': ('status', 'refresh_model_info',)}),
        (_('Header'), {
            'fields': (('title', 'slug'),)}),
        (None, {'fields': ('tagline',)}),
        (_('Content'), {
        	'fields': ('description', ('price', 'price_option'), 'compatibility', 'button_text', 'button_link', 'category')}),
        (_('Featured image'), {
            'fields': ('image',),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Publication'), {
            'fields': (('start_publication', 'end_publication')),
            'classes': ('collapse', 'collapse-open')}),
        (_('Metadata'), {
            'fields': ('featured', 'og_tags'),
            'classes': ('collapse', 'collapse-open')}),
        (_('Author Details'), {
            'fields': ('author', 'author_image', 'company_name', 'company_url', 'company_description',)}))
    list_filter = ('status', 'featured', 'creation_date', 
    	           'start_publication', 'end_publication', 'sites')
    list_display = ('title', 'slug', 'tagline', 'creation_date','status',
    	            'featured', 'sort_order_display')
    radio_fields = {}
    filter_horizontal = ()
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title',)
    actions = ['make_mine', 'make_published',
               'mark_featured', 'unmark_featured']
    actions_on_top = True
    actions_on_bottom = False

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(MatterAppsEntryAdmin, self).__init__(model, admin_site)

    # Custom Display
    def get_title(self, entry):
        """
        Return the title with word count and number of comments.
        """
        title = _('%(title)s (%(word_count)i words)') % \
            {'title': entry.title, 'word_count': entry.word_count}
        return title
    get_title.short_description = _('title')

    def get_queryset(self, request):
        """
        Make special filtering by user's permissions.
        """
        if not request.user.has_perm('mp_blog.can_view_all_models'):
            queryset = self.model.objects.filter(
                status=DRAFT,
            )
        else:
            queryset = super(EntryAdmin, self).get_queryset(request)
        return queryset.prefetch_related('sites',)