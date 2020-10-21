from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Books API", default_version="v1", description="API FOR STX-TASK",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url = "https://rocky-beyond-52741.herokuapp.com/",

)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("book_list.urls")),
    path("api", include("rest_book.urls")),
    path("rest_documentation",schema_view.with_ui("swagger", cache_timeout=0), name="API-DOC")
]
