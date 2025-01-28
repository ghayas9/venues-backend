from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    App configuration class for the 'users' app.
    Handles app-specific settings and initialization logic.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'  # The dotted Python path to the app

    def ready(self):
        """
        Called when the application is ready.
        Used to perform application initialization tasks, such as signal registration.
        """
        import apps.users.signals  # Import and register signals
