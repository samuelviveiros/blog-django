from django.urls import path

from .views import (
    PostList,
    PostDetail,
)

app_name = 'pages'

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:year>/', PostList.as_view(), name='post-list-by-year'),
    path('<int:year>/<int:month>/', PostList.as_view(), name='post-list-by-month'),
    path('<int:year>/<int:month>/<int:day>/', PostList.as_view(), name='post-list-by-day'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
]
