try:
    from django.conf.urls import url as re_path
except ImportError:
    from django.urls import re_path
from . import views

app_name = "v1"
urlpatterns = [
    re_path(r"^$", views.MenuGeneratorIndexView.as_view(), name="index"),
    re_path(r"^main_menu/$", views.MainMenuGeneratorView.as_view(), name="main_menu"),
    re_path(r"^flat_menu/$", views.FlatMenuGeneratorView.as_view(), name="flat_menu"),
    re_path(
        r"^children_menu/$",
        views.ChildrenMenuGeneratorView.as_view(),
        name="children_menu",
    ),
    re_path(
        r"^section_menu/$",
        views.SectionMenuGeneratorView.as_view(),
        name="section_menu",
    ),
]
