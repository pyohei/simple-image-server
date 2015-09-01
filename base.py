# coding: utf8

"""HTTP Base interface.

This module is base for http operation.
"""

import csv
from pyramid.response import Response
from pyramid.renderers import render_to_response

PASSWD = 'hogehoge'
COOKIE = 'mycookie'
MAPPINGS = 'mapping/mapping.txt'


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def _disp_login(request, error='', del_cookies=[]):
    params = {}
    params['error'] = error
    params['hoge'] = 'hoge'
    params['piyo'] = [1, 2, 3, 4]
    response = render_to_response(
        'login.mak',
        params,
        request=request)
    if del_cookies:
        for c in del_cookies:
            response.delete_cookie(c)
    return response


def _disp_images(request):
    params = request.POST
    username = params['username']
    userpass = params['userpass']
    if __can_login(username, userpass):
        image_paths = []
        with open(MAPPINGS, 'rb') as f:
            reader = csv.reader(f)
            for r in reader:
                image_paths.append(r[1])
        params = {}
        params['images'] = image_paths
        response = render_to_response(
            'images.mak',
            params,
            request=request)
        response.set_cookie('sid', 'piyopiyo')
        return response
    return _disp_login(request, u'ログインに失敗しました。')


def _logout(request):
    return _disp_login(request, del_cookies=['sid'])


def __can_login(username, userpass):
    return username == 'piyo' and userpass == 'kumapiyo'


def __has_cookie(cookie):
    pass


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
    config.add_route('images', '/images')
    config.add_view(_disp_images, route_name='images')
    config.add_route('logout', '/logout')
    config.add_view(_logout, route_name='logout')
    config.add_static_view('static', 'static')


if __name__ == '__main__':
    import os
    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
        }
    execute()
