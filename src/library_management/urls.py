from django.conf.urls import url, include
from django.contrib import admin
from .views import library_view, book_view, add_new_book, submit_book



urlpatterns = [
    url(r'^$', library_view, name='library'),
    url(r'^books/(?P<slug>[^\.]+)', book_view , name='books'),
    url(r'^add_new_book/(?P<slug>[^\.]+)', add_new_book , name='add_book'),
    url(r'^submit_book/(?P<slug>[^\.]+)', submit_book , name='add_book'),

]
