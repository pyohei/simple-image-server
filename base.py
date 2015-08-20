# coding: utf8

"""HTTP Base interface.

This module is base for http operation.
"""

from pyramid.response import Response
from pyramid.renderers import render_to_response

PASSWD = 'hogehoge'


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def _disp_login(request):
    responce = render_to_response(
        'login.mak',
        {'hoge': 'p', 'piyo': [1, 2, 3, 4, 5]},
        request=request)
    responce.set_cookie('hoge', 'piyopiyo')
    return responce


def _disp_menu(request):
    return Response('%s' % (",".join(request.cookies)))


def execute():
    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    config = Configurator()
    config.include('pyramid_mako')
    add_routes(config)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8999, app)
    server.serve_forever()


def add_routes(config):
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    config.add_route('login', '/login')
    config.add_view(_disp_login, route_name='login')
    config.add_route('menu', '/menu')
    config.add_view(_disp_menu, route_name='menu')


if __name__ == '__main__':
    import os
    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
        }
    execute()
