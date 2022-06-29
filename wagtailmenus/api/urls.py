try:
    from django.conf.urls import include, url as re_path
except ImportError:
    from django.urls import include, re_path

app_name = "wagtailmenus_api"
urlpatterns = [
    re_path(r"^v1/", include("wagtailmenus.api.v1.urls", namespace="v1")),
]
