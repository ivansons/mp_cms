from django.forms.widgets import CheckboxInput, \
    ClearableFileInput as BaseClearableFileInput


class ClearableFileInput(BaseClearableFileInput):
    """
    Matterport customized ClearableFileInput widget.

    The built-in widget doesn't allow clearing field and uploading new file in
    one operation,which sometime confuses end users.

    This customized widget considers a operation that has both clearing field
    and uploading new file simply as replacing current file.
    """

    def value_from_datadict(self, data, files, name):
        upload = super(BaseClearableFileInput, self).value_from_datadict(
            data, files, name)
        if not upload and not self.is_required \
                and CheckboxInput().value_from_datadict(
                    data, files, self.clear_checkbox_name(name)):
            # False signals to clear any existing value
            return False
        return upload
