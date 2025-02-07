from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    App configuration class for the 'dashboard' app.
    Handles app-specific settings and initialization logic.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.dashboard'  # The dotted Python path to the app

