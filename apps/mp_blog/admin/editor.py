from django.conf import settings

# Code from zinnia-wysiwyg-ckeditor admin.py as it is not compatible if
# ENTRY_BASE_MODEL is extended
if 'ckeditor_uploader' in settings.INSTALLED_APPS:
    from ckeditor_uploader.widgets import CKEditorUploadingWidget as CKEditor
else:
    from ckeditor.widgets import CKEditorWidget as CKEditor
