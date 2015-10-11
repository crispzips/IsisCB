from django import template
from isisdata.models import *
from isisdata.templatetags.app_filters import *

register = template.Library()

@register.filter
def get_page_string(citation):
    if citation.type_controlled != Citation.CHAPTER:
        return ""
    page_start_string = citation.part_details.page_begin
    page_end_string = citation.part_details.page_end
    if page_start_string and page_end_string:
        return "pp. " + str(page_start_string) + "-" + str(page_end_string)
    if page_start_string:
        return "p. " + str(page_start_string)
    if page_end_string:
        return "p. " + str(page_end_string)
    return ""

@register.filter
def join_authors(authors, postfix):
    author_names = []
    for author in authors:
        author_names.append(author.authority.name + postfix)
    return "; ".join(author_names)

@register.filter
def get_editors(citation):
    if citation:
        return citation.acrelation_set.filter(type_controlled__in=['ED'])
    return citation

@register.filter
def join_names_with_postfix(name_list, postfix):
    names = []
    for name in name_list:
        names.append(name + postfix)
    return "; ".join(names)

@register.filter
def get_book_title(citation):
    if citation.type_controlled in ['CH']:
        parent_relation = CCRelation.objects.filter(object_id=citation.id, type_controlled='IC')
        # we assume there is just one
        if parent_relation:
            return parent_relation[0].subject.title

    return ""
