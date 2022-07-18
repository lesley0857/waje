"""wajeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from wajeapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', Book_list_View.as_view(), name='list_book'),
    path('book/<int:id>/', Book_listid_View.as_view(), name='book_detail'),
    path('authors/', Author_list_View.as_view(), name='list_authors'),
    path('author/<int:id>/', Author_listid_View.as_view(), name='list_author'),
    path('author_create', Author_post_View.as_view(), name='author_create'),
    path('book_create', Book_post_View.as_view(), name='book_create'),
    # path('author_put', author_put, name='author_put'),
    # path('books_put/', books_put, name='books_put'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
