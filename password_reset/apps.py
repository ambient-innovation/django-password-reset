from django.apps import AppConfig
from django.conf import settings

try:
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site


class PasswordResetConfig(AppConfig):
    name = 'password_reset'
    DEFAULT_SETTINGS = {
            'token_expires': 3600 * 48,  # Two days
            'get_current_site': get_current_site
    }
    PASSWORD_RESET_SETTINGS = {}

    def ready(self):
        try:
                self.PASSWORD_RESET_SETTINGS = getattr(settings,
                                                      'PASSWORD_RESET_SETTINGS',
                                                       self.DEFAULT_SETTINGS)
        except:
                self.PASSWORD_RESET_SETTINGS = {}

        self.DEFAULT_SETTINGS.update(self.PASSWORD_RESET_SETTINGS)

