from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter
#Create a router and register our view sets with it
router= DefaultRouter(trailing_slash=False)
router.register(r'todos',views.TodoItemViewSet)
# the Api URLS are noew determined automatically by the router
urlpatterns=[ url(r'^',include(router.urls))
              ]
