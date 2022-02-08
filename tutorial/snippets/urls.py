from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from snippets import views
#from rest_framework.urlpatterns import format_suffix_patterns
#from snippets import views

#from snippets.views import SnippetViewSet, UserViewSet, api_root
#from rest_framework import renderers
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url('', include(router.urls)),
]
'''
from django.contrib import admin

urlpatterns = [
    url('snippets/', views.SnippetList.as_view()),
    url('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    url('users/', views.UserList.as_view()),
    url('users/<int:pk>/', views.UserDetail.as_view()),
    
    url('', views.api_root),
    url('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url('api-auth/', include('rest_framework.urls')),
]
'''
# API endpoints
'''
urlpatterns = format_suffix_patterns([
    url('', views.api_root),
    url('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url('users/',
        views.UserList.as_view(),
        name='user-list'),
    url('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])
'''
#urlpatterns = format_suffix_patterns(urlpatterns)

'''
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url('', api_root),
    url('snippets/', snippet_list, name='snippet-list'),
    url('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    url('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    url('users/', user_list, name='user-list'),
    url('users/<int:pk>/', user_detail, name='user-detail')
])
'''