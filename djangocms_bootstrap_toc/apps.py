from django.apps import AppConfig


class DjangoCMSBootstrapTOCConfig(AppConfig):
    name = 'djangocms_bootstrap_toc'
    verbose_name = 'Django CMS Table of Contents'
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        pass
