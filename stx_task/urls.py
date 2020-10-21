from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("book_list.urls")),
    path("api", include("rest_book.urls")),
]
