from django.utils.encoding import force_text


# --- Utility methods for search indexing ---

def prepare_attribute_list(obj, search_attr):
    """
    Prepare a list of a single specific attribute items related to an object

    :param obj: instance with 'attribute' ManyToMany field
    :param search_attr: str

    :return: List of strings

    Notes
    - If search_attr is not an attribute of obj, an empty list is returned

    """
    if hasattr(obj, search_attr):
        return [force_text(k) for k in getattr(obj, search_attr).all()]

    else:
        return []
