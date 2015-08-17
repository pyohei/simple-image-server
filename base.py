# coding: utf8

"""HTTP Base interface.

This module is base for http operation.
"""

from pyramid.response import Response
from pyramid.renderers import render_to_response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def _login(request):
    return render_to_response('login.pt', {}, request=request)


def execute():
    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    config = Configurator()
    add_routes(config)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8999, app)
    server.serve_forever()


def add_routes(config):
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    config.add_route('login', '/login')
    config.add_view(_login, route_name='login')


if __name__ == '__main__':
    execute()