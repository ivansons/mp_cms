from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from filer.fields.file import FilerFileField

import widgy
from widgy.models import Content
from widgy.models.links import LinkField
from widgy.models.mixins import StrDisplayNameMixin, DefaultChildrenMixin
from widgy.utils import SelectRelatedManager
from widgy.contrib.form_builder import models as form_builder_models
from widgy.contrib.page_builder.db.fields import ImageField, VideoField
from widgy.contrib.page_builder import models as page_builder_models
from widgy.contrib.page_builder.models import Html, MainContent, UnsafeHtml

from ..forms import (CallToActionForm, css_style_form_field,
                     modelform_factory, text_form_field)
from ..fields import (HexColorField, IframeTagField,
                      ImageField as CustomImageField)

# Unregister unused built-in widgy
widgy.unregister(form_builder_models.Form)
widgy.unregister(page_builder_models.Accordion)
widgy.unregister(page_builder_models.Button)
widgy.unregister(page_builder_models.Figure)
widgy.unregister(page_builder_models.GoogleMap)
widgy.unregister(page_builder_models.Image)
widgy.unregister(page_builder_models.Section)
widgy.unregister(page_builder_models.Table)
widgy.unregister(page_builder_models.Tabs)
widgy.unregister(page_builder_models.Video)


# Constants
TITLE_SIZE_CHOICES = zip(range(1, 7), range(1, 7))
TEXT_ALIGN_CHOICES = (
    ('center', _('Center')),
    ('left', _('Left')),
    ('right', _('Right')),
)


class BaseMPWidget(Content):
    """
    Base widget
    """
    draggable = True
    deletable = True
    editable = True

    class Meta:
        abstract = True


@widgy.register
class Popup(BaseMPWidget):
    """
    A configurable popup widget
    """

    title = models.CharField(max_length=255, blank=True, default='Title')
    description = models.CharField(max_length=255, blank=True,
                                   default='Description')
    delay = models.IntegerField(
        default=5,
        help_text=_('How many seconds delay to show popup?'))
    recurrence = models.IntegerField(
        default=3,
        help_text=_('Days of recurrence (0 means never).'))
    cookie_name = models.CharField(
        max_length=50, blank=True,
        help_text=_('Identify popup widgets across pages.'))

    class Meta:
        verbose_name = _('popup widget')

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # Popup widgets only go in MainContent
        return isinstance(parent, MainContent)

    def valid_parent_of(self, cls, obj=None):
        return issubclass(cls, Html) or issubclass(cls, UnsafeHtml)

    @property
    def delay_in_milliseconds(self):
        return int(self.delay) * 1000

    @property
    def is_first_of_type(self):
        siblings = self.get_parent().get_children()
        siblings_of_type = [i for i in siblings if isinstance(i, type(self))]
        return siblings_of_type[0] == self

    def get_cookie_name(self):
        return 'mp_popup_{}'.format(
            slugify(self.cookie_name) if self.cookie_name else self.id)


@widgy.register
class TitleTextCta(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to create a title/text/cta section
    """
    accepting_children = True
    tooltip = _('This widget has a title, text and call-to-action button')

    # title, HTML_only boolean, text, & color/size elements
    title = models.CharField(max_length=255, blank=True, default='Title')
    title_color = HexColorField(blank=True)
    title_size = models.IntegerField(blank=True, null=True, default=2,
                                     choices=TITLE_SIZE_CHOICES)
    text_is_raw_html = models.BooleanField(default=False)
    text = models.TextField(blank=True, default='Text')
    text_color = HexColorField(blank=True)

    class Meta:
        verbose_name = _('title text block')

    @property
    def default_children(self):
        """
        Adds 1 call-to-action
        """
        return [
            (Cta, (), {'text': _('CTA Text'), 'url': _('#')}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts CallToActions
        return issubclass(cls, Cta)

    @property
    def title_tag(self):
        return 'h{}'.format(self.title_size or 2)


@widgy.register
class Cta(BaseMPWidget):
    """
    widget to create a single call to action hyperlink button
    """
    accepting_children = False
    tooltip = _('This widget has a call-to-action button')

    text = models.CharField(verbose_name=_('CTA text'), max_length=255,
                            blank=True, default='CTA text')
    url = models.CharField(verbose_name=_('CTA url'), max_length=255,
                           blank=True, default='CTA url')

    class Meta:
        verbose_name = _('CTA')


@widgy.register
@python_2_unicode_compatible
class CallToAction(StrDisplayNameMixin, Content):
    editable = True
    tooltip = _('Add a link to another page')
    form = CallToActionForm
    objects = SelectRelatedManager(prefetch_related=['link'])

    text = models.CharField(max_length=255, verbose_name=_('text'), blank=True)
    link = LinkField(null=True)

    class Meta:
        verbose_name = _('CTA Button')

    def __str__(self):
        return self.text or ''


class BaseImageTitleTextCta(DefaultChildrenMixin, BaseMPWidget):
    """
    abstract base widget to create an imagetitletextcta
    """
    accepting_children = True

    image = ImageField(verbose_name=_('Image'), blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def default_children(self):
        """
        Adds 1 TitleTextCta
        """
        return [
            (TitleTextCta, (), {}),
        ]

    @property
    def parent_cls_name(self):
        return type(self.get_parent()).__name__


@widgy.register
class ImageTitleTextCta(BaseImageTitleTextCta):
    """
    widget to create image, title, text and CTA. It's rendered differently
    depending on its parent, which could be TwoUpOverlay, ThreeUpIcon,
    ThreeUpOverlay, or ThreeUpLongText.
    """
    tooltip = _('This widget has a image, title, text and call-to-action')

    class Meta:
        verbose_name = _('Image content block')


class BaseFeatureSection(DefaultChildrenMixin, BaseMPWidget):
    """
    abstract widget to support Feature Section widget patterns
    """
    accepting_children = True

    # images and background color
    background_image = ImageField(verbose_name=_('Background image'),
                                  blank=True, null=True)
    background_color = HexColorField(blank=True)
    # content on left or right
    text_content_is_on_left = models.BooleanField(default=True)
    # css customization
    css_class = models.CharField(verbose_name=_('CSS class'), max_length=255,
                                 blank=True, default='')
    css_style = models.TextField(verbose_name=_('CSS style'), blank=True,
                                 default='')

    form = modelform_factory('BaseFeatureSectionForm',
                             css_style=css_style_form_field)

    class Meta:
        abstract = True

    @property
    def default_children(self):
        """
        Adds 1 TitleTextCta
        """
        return [
            (TitleTextCta, (), {}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts TitleTextCallToAction
        return issubclass(cls, TitleTextCta) or issubclass(cls, Html) or \
               issubclass(cls, UnsafeHtml)


@widgy.register
class FeatureSection(BaseFeatureSection):
    """
    widget to support patterns such as:
    Feature Section (right image),
    Feature Section (left image),
    Feature Section (right content + photo overlay),
    Feature Section (left content + photo overlay),
    Background Picture and  Right Content.(additional Hyperlinks),
    Background Picture with Right Content.(Two Hyperlink),
    Background Picture with Right Content.(Three Hyperlink)
    """
    tooltip = _('This widget has background image, image, text, title, and '
                'call-to-action')

    foreground_image = ImageField(verbose_name=_('Foreground image'),
                                  blank=True, null=True)
    # large image flag
    large_image = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('feature section')


@widgy.register
class FeatureSectionVideo(BaseFeatureSection):
    """
    widget to support Feature Section (video)
    """
    tooltip = _('This widget has background image, video, text, title, and '
                'call-to-action')
    # video
    iframe_tag = IframeTagField(verbose_name=_('iFrame Tag'), blank=True,
                                default='<iframe></iframe>')

    class Meta:
        verbose_name = _('feature section video')


class BaseTitle(BaseMPWidget):
    """
    abstract widget that has a title and background color
    """
    accepting_children = True

    background_color = HexColorField(blank=True)
    # title and color
    main_title = models.CharField(verbose_name=_('Main title'), max_length=255,
                                  blank=True, default='Main Title')
    main_title_color = HexColorField(blank=True)
    # css customization & background color
    css_class = models.CharField(verbose_name=_('CSS class'), max_length=255,
                                 blank=True, default='')
    css_style = models.TextField(verbose_name=_('CSS style'), blank=True,
                                 default='')

    form = modelform_factory('BaseFeatureSectionForm',
                             css_style=css_style_form_field)

    class Meta:
        abstract = True

    def get_css_style(self):
        style_list = []
        if self.css_style:
            style_list.append(self.css_style.strip(' ;'))
        if self.background_color:
            style_list.append('background-color: {}'.format(
                    self.background_color))
        return '; '.join(style_list)


class BaseUp(DefaultChildrenMixin, BaseTitle):
    """
    abstract widget to support 2-Up and 3-Up widget patterns, MSP Member
    Materials
    """
    # text and color
    main_text = models.CharField(verbose_name=_('Main text'), max_length=1000,
                                 blank=True, default='Main Text')
    main_text_color = HexColorField(blank=True)
    # main text raw html
    main_text_is_raw_html = models.BooleanField(
            verbose_name=_('Is main text raw HTML?'),
            default=False)
    # main title size
    main_title_size = models.IntegerField(
            verbose_name=_('Main Title Size (h1~h6)'),
            choices=TITLE_SIZE_CHOICES, default=2)
    main_title_is_raw_html = models.BooleanField(
            verbose_name=_('Is main title raw HTML?'),
            default=False)
    # text alignment
    text_align = models.CharField(verbose_name=_('Text alignment'),
                                  max_length=32, default='left',
                                  choices=TEXT_ALIGN_CHOICES)

    form = modelform_factory('BaseUpForm',
                             css_style=css_style_form_field,
                             main_text=text_form_field)

    class Meta:
        abstract = True

    @property
    def main_title_tag(self):
        return 'h{}'.format(self.main_title_size)


@widgy.register
class Section(BaseUp):
    """
    widget to provide a container for a section of content
    """
    # background image
    background_image = ImageField(verbose_name=_('Background image'),
                                  blank=True, null=True)

    class Meta:
        verbose_name = _('Section Container')

    def get_css_style(self):
        style_list = [
            'text-align: {}'.format(self.text_align)
        ]
        if self.css_style:
            style_list.append(self.css_style.strip(' ;'))
        if self.background_color:
            style_list.append('background-color: {}'.format(
                    self.background_color))
        if self.background_image:
            style_list.append('background-image: url({})'.format(
                    self.background_image.url))
            style_list += ['background-repeat: no-repeat',
                           'background-size: cover']
        return '; '.join(style_list)


@widgy.register
class TwoUpOverlay(BaseUp):
    """
    widget to support 2-UP A (photo overlays)
    """
    tooltip = _('This widget has title and text on top, then 2 vertical '
                'sections underneath each with image, overlayed title, '
                'overlayed text, and overlayed call-to-action')

    class Meta:
        verbose_name = _('2-up overlay')

    @property
    def default_children(self):
        """
        Adds 2 ImageTitleTextCta children
        """
        return [
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
        ]


@widgy.register
class TwoUpEmbedCode(BaseUp):
    """
    widget to support 2-Up with text and embed underneath image
    """
    tooltip = _('This widget has title and text on top, then 2 vertical '
                'sections underneath each with image, title, '
                'text, call-to-action for model view, and embedded code text')

    embed_code_text1 = models.CharField(verbose_name=_('Embed Code Text 1'),
                                        max_length=255, blank=True,
                                        default='Copy Embed Code')
    data_model_id1 = models.CharField(verbose_name=_('Data Model ID 1'),
                                      max_length=255, blank=True)
    embed_code_text2 = models.CharField(verbose_name=_('Embed Code Text 2'),
                                        max_length=255, blank=True,
                                        default='Copy Embed Code')
    data_model_id2 = models.CharField(verbose_name=_('Data Model ID 2'),
                                      max_length=255, blank=True)

    class Meta:
        verbose_name = _('2-up embed code')

    @property
    def default_children(self):
        """
        Adds 2 ImageTitleTextCta children
        """
        return [
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
        ]


@widgy.register
class ThreeUpIcon(BaseUp):
    """
    widget to support patterns such as:
    3-Up A (with hyperlink),
    3-Up B (without hyperlink),
    """
    tooltip = _('This widget has title and text on top, then 3 vertical '
                'sections underneath each with image, title, text, and '
                'call-to-action')

    class Meta:
        verbose_name = _('3-up icon')

    @property
    def default_children(self):
        """
        Adds 3 ImageTitleTextCta children
        """
        return [
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
        ]


@widgy.register
class ThreeUpOverlay(BaseUp):
    """
    widget to support patterns such as:
    3-Up C (photo overlay with call-to-action),
    3-Up D (photo overlay without call-to-action),
    """
    tooltip = _('This widget has title and text on top, then 3 vertical '
                'sections underneath each with image, overlayed title, '
                'overlayed text, and overlayed call-to-action')

    class Meta:
        verbose_name = _('3-up overlay')

    @property
    def default_children(self):
        """
        Adds 3 ImageTitleTextCta children
        """
        return [
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
        ]


@widgy.register
class ThreeUpImage(BaseUp):
    """
    widget to support patterns such as:
    three video (image) with content
    """
    tooltip = _('This widget has title and text on top, a single centered '
                'call-to-action button on bottom, then 3 vertical sections in '
                'the middle each with image and title.')

    class Meta:
        verbose_name = _('3-up image')

    @property
    def default_children(self):
        """
        Adds 3 ImageTitleTextCta children
        """
        return [
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
            (SingleCta, (), {}),
        ]


@widgy.register
class ThreeUpLongText(BaseUp):
    """
    widget to support 3-Up E (Long text without hyperlinks)
    """
    tooltip = _('This widget has title and text on top, then 3 vertical '
                'sections underneath each with image, title, long text, and '
                'call-to-action')

    class Meta:
        verbose_name = _('3-up long text')

    @property
    def default_children(self):
        """
        Adds 3 TitleTextCta children
        """
        return [
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
            (ImageTitleTextCta, (), {}),
        ]


@widgy.register
class Quotes(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to support Quote pattern (Background image with carousel)
    """
    accepting_children = True
    tooltip = _('This widget has background image, title & text carousel and '
                'bottom HTML region where logos can be placed')

    # background image
    background_image = ImageField(verbose_name=_('Background image'),
                                  blank=True, null=True)

    class Meta:
        verbose_name = _('quotes')

    @property
    def default_children(self):
        """
        Adds 1 HTML section and 2 Single Quotes as children to initially
        populate the carousel of quotes.
        """
        return [
            (Html, (), {}),
            (SingleQuote, (), {'title': _('Title 1'),
                               'subtitle': _('Subtitle 1')}),
            (SingleQuote, (), {'title': _('Title 2'),
                               'subtitle': _('Subtitle 2')}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts SingleQuote
        return issubclass(cls, SingleQuote) or issubclass(cls, Html)


@widgy.register
class SingleQuote(BaseMPWidget):
    """
    widget to create a single quote in the carousel of the 'Quotes' widget
    """
    tooltip = _('This widget has title and text and is a child of Quote')

    title = models.CharField(verbose_name=_('Title'), max_length=255,
                             blank=True, default='Title')
    title_color = HexColorField(blank=True)
    subtitle = models.CharField(verbose_name=_('Sub-title'), max_length=255,
                                blank=True, default='Sub-title')
    subtitle_color = HexColorField(blank=True)

    class Meta:
        verbose_name = _('single quote')

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # SingleQuote widgets only go in Quotes and Stats
        return isinstance(parent, Quotes) or isinstance(parent, Stats)


@widgy.register
class SingleCta(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to support one centered call-to-action button that will be
    placed at the bottom of different sections
    """
    accepting_children = True
    tooltip = _('This widget has one centered call-to-action')

    # css customization
    css_class = models.CharField(verbose_name=_('CSS class'), max_length=255,
                                 blank=True, default='inside')

    class Meta:
        verbose_name = _('Single CTA')

    @property
    def default_children(self):
        """
        Adds 1 call-to-action
        """
        return [
            (Cta, (), {'text': _('CTA Text'), 'url': _('#')}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts CallToActions
        return issubclass(cls, Cta)


@widgy.register
class ThreeCta(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to support three horizontal call-to-action buttons that will be
    placed at the bottom of different pages
    """
    accepting_children = True
    tooltip = _('This widget has three horizontal call-to-actions')

    class Meta:
        verbose_name = _('3 CTA')

    @property
    def default_children(self):
        """
        Adds 3 call-to-actions
        """
        return [
            (Cta, (), {'text': _('CTA Text'), 'url': _('#')}),
            (Cta, (), {'text': _('CTA Text'), 'url': _('#')}),
            (Cta, (), {'text': _('CTA Text'), 'url': _('#')}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts CallToActions
        return issubclass(cls, Cta)


@widgy.register
class CustomerStories(DefaultChildrenMixin, BaseTitle):
    """
    widget to support carousel with slides from Customer Story and Customer
    Story (video)
    """
    tooltip = _('This widget has a carousel of customer stories')

    class Meta:
        verbose_name = _('customer stories')

    @property
    def default_children(self):
        """
        Adds 1 customer story slide and 1 customer story video slide
        """
        return [
            (CustomerStorySlide, (), {}),
            (CustomerStoryVideoSlide, (), {})
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts CustomerStory and CustomerStoryVideo
        return issubclass(cls, CustomerStorySlide) or \
            issubclass(cls, CustomerStoryVideoSlide)


class BaseCustomerStorySlide(BaseImageTitleTextCta):
    """
    base widget for customer story slides
    """
    @classmethod
    def valid_child_of(cls, parent, obj=None):

        # CustomerStorySlide widgets only go in CustomerStories
        return isinstance(parent, CustomerStories)

    customer_quote = models.CharField(verbose_name=_('Customer quote'),
                                      max_length=255, blank=True,
                                      default='Customer quote')
    customer_quote_color = HexColorField(blank=True)

    class Meta:
        abstract = True


@widgy.register
class CustomerStorySlide(BaseCustomerStorySlide):
    """
    widget to support customer story slide
    """
    tooltip = _('This widget is a single customer story slide')

    class Meta:
        verbose_name = _('customer story slide')

    @property
    def default_children(self):
        """
        Adds 1 TitleTextCta for left side and 1 Html section for
        right side for text and link
        """
        return [
            (TitleTextCta, (), {}),
            (Html, (), {}),
        ]


@widgy.register
class CustomerStoryVideoSlide(BaseCustomerStorySlide):
    """
    widget to support customery story video slide
    """
    tooltip = _('This widget is a single customer story video slide')

    video = VideoField(verbose_name=_('Video'), blank=True, null=True)
    video_background_image = ImageField(
        verbose_name=_('Video background image'), blank=True, null=True)

    class Meta:
        verbose_name = _('customer story video slide')


@widgy.register
class Stats(BaseUp):
    """
    widget to support Stats pattern
    """
    tooltip = _('This widget has a statistics')

    background_image = ImageField(verbose_name=_('Background image'),
                                  blank=True, null=True)

    class Meta:
        verbose_name = _('stats')

    @property
    def default_children(self):
        """
        Adds 3 stat sections
        """
        return [
            (SingleQuote, (), {}),
            (SingleQuote, (), {}),
            (SingleQuote, (), {}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts SingleQuote children
        return issubclass(cls, SingleQuote)

    def get_css_style(self):
        style_list = [
            'text-align: {}'.format(self.text_align)
        ]
        if self.css_style:
            style_list.append(self.css_style.strip(' ;'))
        if self.background_color:
            style_list.append('background-color: {}'.format(
                    self.background_color))
        if self.background_image:
            style_list.append('background-image: url({})'.format(
                    self.background_image.url))
            style_list += ['background-repeat: no-repeat',
                           'background-size: cover']
        return '; '.join(style_list)


@widgy.register
class Hero(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to support Hero
    """
    accepting_children = True
    tooltip = _('This widget has background image and video,'
                'with title & text carousel on right and Title & Text on Left')

    # Image for Video
    bg_image = ImageField(verbose_name=_('background image'),
                          blank=True, null=True, related_name='maps')
    # Video (Link from Vimeo)
    bg_video_url = models.CharField(verbose_name=_('background video url'),
                                    max_length=255, blank=True,
                                    default='video url')


@widgy.register
class HeroRightContent(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to support Hero
    """
    accepting_children = True
    tooltip = _('This widget has title & text carousel for '
                'Right content of Hero')

    class Meta:
        verbose_name = _('Hero RightContent')

    @property
    def default_children(self):
        """
        Adds RightContent as children to initially
        populate the carousel of HeroRightContent.
        """

        return [
            (RightContent, (), {'title': _('Title 1'),
                                'text': _('Text 1')}),
            (RightContent, (), {'title': _('Title 2'),
                                'text': _('Text 2')}),
        ]

    def valid_parent_of(self, cls, obj=None):
        # only accepts RightContent
        return issubclass(cls, RightContent)

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # HeroRightContent widget only go in Hero
        return isinstance(parent, Hero)


@widgy.register
class RightContent(BaseMPWidget):
    """
    widget to create a Right content carousel in 'HeroRightContent' widget
    """
    tooltip = _('This widget has title and text and is a child '
                'of HeroRightContent')

    title = models.CharField(verbose_name=_('Title'), max_length=255,
                             blank=True, default='Title')
    text = models.CharField(verbose_name=_('Text'), max_length=255,
                            blank=True, default='Text')

    class Meta:
        verbose_name = _('RightContent Carousel')

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # RightContent widget only go in HeroRightContent
        return isinstance(parent, HeroRightContent)


@widgy.register
class HeroLeftContentA(DefaultChildrenMixin, BaseMPWidget):
    """
    Left Content of hero widget
    """
    accepting_children = True
    tooltip = _('This widget has title,text and CTA for Left content of Hero')

    class Meta:
        verbose_name = _('Hero Left Content A')

    @property
    def default_children(self):
        """
        Adds 1 TitleTextCta
        """
        return [
            (TitleTextCta, (), {}),
        ]

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # HeroLeftContentA widget only go in Hero and Section
        return isinstance(parent, Hero) or isinstance(parent, Section)


@widgy.register
class HeroLeftContentB(DefaultChildrenMixin, BaseMPWidget):
    """
    Left Content of hero widget
    """
    accepting_children = True
    tooltip = _('This widget has title,text and CTA for Left content of Hero')
    pop_up_video_iframe_tag = IframeTagField(
        verbose_name=_('Pop-up Video iFrame Tag'), blank=True,
        default='<iframe></iframe>')

    class Meta:
        verbose_name = _('Hero Left Content B')

    @property
    def default_children(self):
        """
        Adds 1 TitleTextCta
        """
        return [
            (TitleTextCta, (), {}),
        ]

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # HeroLeftContentB widget only go in Hero and Section
        return isinstance(parent, Hero) or isinstance(parent, Section)


@widgy.register
class SixUp(BaseUp):
    """
    widget to Six-Up (titled images)
    """
    accepting_children = True
    tooltip = _('This widget has title & text with six titled images')

    class Meta:
        verbose_name = _('6-Up')

    @property
    def default_children(self):
        """
        Adds SixUpContent as children to SixUp.
        """
        return [
            (SixUpContent, (), {}),
            (SixUpContent, (), {}),
            (SixUpContent, (), {}),
            (SixUpContent, (), {}),
            (SixUpContent, (), {}),
            (SixUpContent, (), {}),
        ]

    def valid_parent_of(self, cls, obj=None):
        return issubclass(cls, SixUpContent)


@widgy.register
class SixUpContent(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to create a content block for SixUp widget
    """
    tooltip = _('This widget has Image,title and hyperlink '
                'and is a child of SixUp')

    image = ImageField(verbose_name=_('Image'), blank=True, null=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255,
                             blank=True, default='Title')
    url_text = models.CharField(verbose_name=_('url Text'), max_length=255,
                                blank=True, default='url Text')
    url = models.CharField(verbose_name=_('url'), max_length=255,
                           blank=True, default='url')

    class Meta:
        verbose_name = _('6-Up Content')

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # SixUpContent widget only go in SixUp
        return isinstance(parent, SixUp)


@widgy.register
class TabPanel(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to create a tab and its content panel within a TabPanelContainer
    """
    accepting_children = True

    # title of nav tab
    title = models.CharField(verbose_name=_('Title'), max_length=255,
                             blank=True, default='Title')
    # hashtag of nav tab
    hashtag = models.CharField(
        verbose_name=_('Hashtag'), max_length=32, blank=True, default='',
        help_text=_('Each tab panel nees a unique hashtag'))
    # icon of nav tab
    icon = CustomImageField(
        verbose_name=_('Icon image'), blank=True, null=True,
        accepted_files=['.jpg', '.jpeg', '.png', '.gif', '.ico'])

    class Meta:
        verbose_name = _('Tab Panel')

    @property
    def default_children(self):
        """
        Adds 1 UnsafeHtml
        """
        return [
            (UnsafeHtml, (), {}),
        ]

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # TabPanel widget only go in TabPanelContainer
        return isinstance(parent, TabPanelContainer)

    def get_hashtag(self):
        return self.hashtag.strip('#') or 'panel-{}'.format(self.id)


@widgy.register
class TabPanelContainer(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to create a TabPanelContainer of switchable tab panels.
    """
    accepting_children = True
    editable = False

    class Meta:
        verbose_name = _('Tab Panel Container')

    @property
    def default_children(self):
        """
        Adds 3 TabPanel
        """
        return [
            (TabPanel, (), {}),
            (TabPanel, (), {}),
            (TabPanel, (), {}),
        ]

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # TabPanelContainer widget only go in Section, Row, and Column
        return type(parent) in {Section, Row, Column}

    def valid_parent_of(self, cls, obj=None):
        # only accepts TabPanel
        return issubclass(cls, TabPanel)


@widgy.register
class Column(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to create a column container in row container.
    """
    WIDTH_CHOICES = (
        ('1/3', _('1/3 of row')),
        ('1/2', _('1/2 of row')),
        ('2/3', _('2/3 of row')),
        ('3/3', _('3/3 of row')),
    )

    accepting_children = True
    editable = True

    width = models.CharField(verbose_name=_('Column width'), max_length=50,
                             choices=WIDTH_CHOICES, default='1/2')

    class Meta:
        verbose_name = _('Column in row')

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # Column widget only go in Row
        return isinstance(parent, Row)

    def get_css_class(self):
        css_map = {
            '1/3': 'col-md-4',
            '1/2': 'col-md-6',
            '2/3': 'col-md-8',
            '3/3': 'col-md-12',
        }
        return css_map[self.width]


@widgy.register
class Row(DefaultChildrenMixin, BaseMPWidget):
    """
    widget to create a row container that holds column container.
    """
    accepting_children = True

    use_side_padding = models.BooleanField(
        verbose_name=_('Padding both sides'), default=True)

    class Meta:
        verbose_name = _('Row container')

    @property
    def default_children(self):
        """
        Adds 3 Column
        """
        return [
            (Column, (), {'width': '1/2'}),
            (Column, (), {'width': '1/2'}),
        ]

    @classmethod
    def valid_child_of(cls, parent, obj=None):
        # Row widget only goes in Section
        return type(parent) in {Section, Column}


@widgy.register
class DownloadFile(BaseMPWidget):
    """
    downloadable file widget
    """
    name = models.CharField(max_length=255)
    download_file = FilerFileField(null=True, blank=True)
    download_link = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _('Download File')

    def get_download_url(self):
        if self.download_file:
            return self.download_file.url
        else:
            return self.download_link

    def is_download(self):
        if self.download_file:
            return True
        return False


@widgy.register
class MspMaterial(BaseUp):
    """
    widget to support MSP Intranet Member Materials / Videos
    """
    # left header text
    upper_left_text = models.CharField(verbose_name=_('Upper left text'),
                                       max_length=255, blank=True)
    # image
    image = CustomImageField(
        verbose_name=_('Right image'), blank=True, null=True,
        accepted_files=['.jpg', '.jpeg', '.png', '.gif', '.ico'])
    # video
    iframe_tag = IframeTagField(verbose_name=_('iFrame Tag'), blank=True,
                                default='<iframe></iframe>')

    class Meta:
        verbose_name = _('MSP Material')

    @property
    def default_children(self):
        """
        Adds DownloadFile
        """
        return [
            (DownloadFile, (), {}),
        ]


@widgy.register
class MspWebinarEvent(BaseMPWidget):
    """
    widget to support MSP Intranet Webinars & Events
    """
    # Main title
    main_title = models.CharField(verbose_name=_('Main title'),
                                  max_length=255, default='Webinar')
    # Main text
    main_text = models.CharField(verbose_name=_('Main text'),
                                 max_length=255, blank=True,
                                 default='WEDNESDAY, AUG 10, 2016 | 11 AM PT '
                                         '| DURATION: 1H')
    # Secondary text
    sub_text = models.CharField(verbose_name=_('Secondary text'),
                                max_length=255, blank=True,
                                default='Topic Coming Soon')
    # Register Now text
    register_text = models.CharField(verbose_name=_('Register Now text'),
                                     max_length=255, blank=True,
                                     default="Register Now")
    # Register Now link
    register_link = models.URLField(verbose_name=_('Register Now link'),
                                    blank=True)

    class Meta:
        verbose_name = _('MSP Webinar Event')

