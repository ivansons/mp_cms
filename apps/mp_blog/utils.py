from cStringIO import StringIO
import hashlib

from django.core.files.images import ImageFile

import PIL
from filer.models import Image
import requests


def generate_sha1(file_obj):
    sha = hashlib.sha1()
    file_obj.seek(0)
    while True:
        buf = file_obj.read(104857600)
        if not buf:
            break
        sha.update(buf)
    # to make sure later operations can read the whole file
    file_obj.seek(0)
    return sha.hexdigest()


def detect_image_format(file_obj):
    file_obj.seek(0)
    image = PIL.Image.open(file_obj)
    image_format = image.format
    file_obj.seek(0)
    return image_format.lower()


def generate_image_filename(file_obj):
    """
    Generate a filename for image based on image's sha1 and format.
    """
    return '%s.%s' % (generate_sha1(file_obj), detect_image_format(file_obj))


def upload_image_to_s3(image_url):
    """
    Download image from a given `image_url` and upload to Amazon S3.

    :param image_url: URL of image to download
    :return: django-filer Image object
    """
    response = requests.get(image_url)

    file_obj = ImageFile(StringIO(response.content))
    file_name = generate_image_filename(file_obj)
    file_obj.name = file_name

    image = Image.objects.create(
        original_filename=file_name,
        file=file_obj)

    return image
