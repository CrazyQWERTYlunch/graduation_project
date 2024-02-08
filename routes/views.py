from django.shortcuts import render

from .models import Route


def view_routes(request):
    routes = Route.objects.all()

    context = {
        'title': 'Маршруты',
        'routes': routes
    }

    return render(request, 'routes/routes.html', context)


def route(request, route_slug=False):
    if route_slug:
        route = Route.objects.get(slug=route_slug)
    
    context = {
        'route': route
    }

    return render(request, 'routes/route.html', context)