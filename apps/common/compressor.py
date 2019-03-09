# -*- coding: utf8 -*-
"""
Matterport-specific precompiler for scss

By default, `cache_buster` option is used when compiling scss files, which
generates dynamic urls. This conflicts with our process of deployment.

In our process, the static files are generated and uploaded into S3 during
building time. To keep the static files consistent among different web
servers, it's better to have them generate same files when running command -
`python manager.py compress`.

Thus, we override `cache_buster` settings by injecting customized functions
into the default namespace.
"""

from django_pyscss.compressor import DjangoScssFilter
from django_pyscss.extension.django import DjangoExtension

from scss.extension.compass import helpers, images, sprites

ns = DjangoExtension.namespace


@ns.declare
def font_url(path, only_path=False, cache_buster=False):
    return helpers.font_url(path, only_path=only_path,
                            cache_buster=cache_buster)


@ns.declare
def image_url(path, only_path=False, cache_buster=False, dst_color=None,
              src_color=None, spacing=None, collapse_x=None, collapse_y=None):
    return images.image_url(path, only_path=only_path,
                            cache_buster=cache_buster, dst_color=dst_color,
                            src_color=src_color, spacing=spacing,
                            collapse_x=collapse_x, collapse_y=collapse_y)


@ns.declare
def sprite(map, sprite, offset_x=None, offset_y=None, cache_buster=False):
    return sprites.sprite(map, sprite, offset_x=offset_x,
                          offset_y=offset_y, cache_buster=cache_buster)


@ns.declare
def sprite_map(g, **kwargs):
    kwargs.update({
        'cache_buster': False,
    })
    return sprites.sprite_map(g, **kwargs)


@ns.declare
def sprite_url(map, cache_buster=False):
    return sprites.sprite_url(map, cache_buster=False)


@ns.declare
def stylesheet_url(path, only_path=False, cache_buster=False):
    return helpers.stylesheet_url(path, only_path=only_path,
                                  cache_buster=cache_buster)


@ns.declare
def twbs_font_path(path):
    return helpers._font_url(path, False, False, False)


@ns.declare
def twbs_image_path(path):
    return images._image_url(path, False, False, None, None, False, None,
                             None, None, None)


# Todo - these functions may need override.
"""
@ns.declare
def font_files(*args):
    return _font_files(args, inline=False)


@ns.declare
def inline_font_files(*args):
    return _font_files(args, inline=True)
"""
