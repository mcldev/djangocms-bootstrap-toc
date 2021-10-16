from django.db import models
from django.template.defaultfilters import force_escape
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# https://afeld.github.io/bootstrap-toc/

class BootstrapTableOfContents(CMSPlugin):
    """
    Info to display a table of contents for a page
    """
    scope_filter_elements = models.CharField(_('Elements Within Tag'), max_length=250, blank=True, null=True,
                                             default="main",
                                             help_text=_(
                                                 'Filter heading elements within selected tags only, .e.g $("main h1, main h2")'))
