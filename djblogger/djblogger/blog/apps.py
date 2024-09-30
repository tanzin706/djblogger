from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    #name changed from blog -> djblogger.blog
    name = "djblogger.blog"
