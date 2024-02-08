from django.urls import path
from routes import views

app_name = 'routes'

urlpatterns = [
    path('', views.view_routes, name='view_routes'),
    path('route/<slug:route_slug>/', views.route, name='route'),
]
