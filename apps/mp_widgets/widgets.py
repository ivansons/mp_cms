from django.conf import settings
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe

# Set colors needed for Marketing Team here
DEFAULT_PALETTE_COLORS = \
    ['000000', 'FFFFFF', '1d3742', '00a8e6', '0098ff', '4d4d4d', '002f40',
     'f3f3f3', 'd1d3d4', '5c5c5c', 'dedede', '002836', 'ebebeb', 'c4c4c4',
     'f6f6f6', 'faac17']


class ColorPickerWidget(TextInput):
    class Media:
        css = {
            'all': ('colorful/colorPicker.css', 'css/colorful_overwrite.css')
        }
        js = ('colorful/jQuery.colorPicker.js',)

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs={}):
        if 'id' not in attrs:
            attrs['id'] = "id_%s" % name

        js = '''<script type="text/javascript">
                  (function($){
                    $(document).ready(function(){
                      $('#%s').each(function(i, elm){
                        $.fn.colorPicker.defaultColors = %s;
                        $(elm).colorPicker();
                      });
                    });
                  })('django' in window && django.jQuery ? django.jQuery: jQuery);
                </script>''' % (attrs['id'], str(DEFAULT_PALETTE_COLORS))

        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(js)
