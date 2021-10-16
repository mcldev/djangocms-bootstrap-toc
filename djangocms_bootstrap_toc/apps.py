from django.apps import AppConfig


class DjangoCMSBootstrapTOCConfig(AppConfig):
    name = 'djangocms_bootstrap_toc'
    verbose_name = 'Django CMS Table of Contents'

    def ready(self):
        pass
