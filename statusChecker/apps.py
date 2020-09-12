from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'statusChecker'

    def ready(self):
        import statusChecker.signals