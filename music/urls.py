from django.urls import path
from .views import ListSongsView, PostSongsView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs-add/', csrf_exempt(PostSongsView.as_view()), name="songs-all")

]
