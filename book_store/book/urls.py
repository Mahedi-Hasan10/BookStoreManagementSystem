from django.urls import path
from book.views import home,store_book,edit_book,show_book,delete_book
urlpatterns = [
    path('',home,name='homepage'),
    path('store/',store_book,name='storebook'),
    path('edit/',edit_book,name='editbook'),
    path('show/',show_book,name='showbook'),
    path('edit_book/<int:id>',edit_book,name='editbook'),
    path('delete_book/<int:id>',delete_book,name='deletebook')
]
