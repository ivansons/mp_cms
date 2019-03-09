from django.core.validators import RegexValidator
import re


class HexColorValidator(RegexValidator):
    regex = '^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    message = 'Please enter a valid hex color code, such as #fff or #060606.'

validate_hex_color = HexColorValidator()


class IframeTagValidator(RegexValidator):
    """
    Validator for IframeTagField (Feature Section Video)

    Ensures that the iframe tag:
    1. utilizes 'https' in the src of the embedded player
    2. applies the api=1 key query parameter
    """
    regex = re.compile('^(<iframe[\s\S]+></iframe>)',
                       re.IGNORECASE)

    message = 'Please enter a valid iframe tag such as: <iframe' \
              ' src="https://player.vimeo.com/video/88954819?api=1"' \
              ' frameborder="0" seamless allowfullscreen width="918"' \
              ' height="514"></iframe>'

validate_iframe_tag = IframeTagValidator()
