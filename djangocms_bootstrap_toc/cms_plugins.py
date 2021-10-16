from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import BootstrapTableOfContents


class BootstrapTableOfContentsPlugin(CMSPluginBase):
    model = BootstrapTableOfContents
    name = _("Bootstrap Table of Contents")

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_bootstrap_toc/bootstrap-toc.html'

    def render(self, context, instance, placeholder):
        context.update({
            'inst': instance,
            'scope': instance.scope_filter_elements,
        })
        return context


plugin_pool.register_plugin(BootstrapTableOfContentsPlugin)
