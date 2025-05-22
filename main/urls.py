from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre-mi'),
    path('servicios/', views.servicios, name='servicios'),
    path('recetas/', views.recetas, name='recetas'),
    path('eventos/', views.eventos, name='eventos'),
    path('contacto/', views.contacto, name='contacto'),
    path('blog/', PostListView.as_view(),  name='post_list'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
