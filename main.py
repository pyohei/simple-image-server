"""HTTP Base interface.

This module is base for http operation.
"""

import csv
from pyramid.renderers import render_to_response

USER = 'user'
PASSWD = 'password'
COOKIE = 'mycookie'
MAPPINGS = 'sample/mapping.txt'
RLEASE_MODE = False


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
    is_login = False
    if 'username' in params and 'userpass' in params:
        username = params['username']
        userpass = params['userpass']
        is_login = __can_login(username, userpass)
    if 'sid' in request.cookies:
        sid = request.cookies['sid']
        is_login = __has_valid_cookie(sid)
    if not is_login:
        return _disp_login(request, u'Failur in login!!!')
    image_paths = []
    with open(MAPPINGS, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            image_paths.append(r[1])
    params = {}
    params['images'] = image_paths
    response = render_to_response(
        'images.mak',
        params,
        request=request)
    response.set_cookie('sid', 'iv')
    return response


def _logout(request):
    return _disp_login(request, del_cookies=['sid'])


def __can_login(username, userpass):
    return username == USER and userpass == PASSWD


def __has_valid_cookie(cookie):
    return cookie == 'iv'


def __add_routes(config):
    """ Add Root information."""
    config.add_route('login', '/login')
    config.add_view(_disp_login, route_name='login')
    config.add_route('images', '/images')
    config.add_view(_disp_images, route_name='images')
    config.add_route('logout', '/logout')
    config.add_view(_logout, route_name='logout')
    config.add_static_view('static', 'static')
    if RLEASE_MODE:
        config.add_static_view('photos', '/var/www/photos')


def execute():
    """ Execute this application."""
    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    config = Configurator()
    config.include('pyramid_mako')
    __add_routes(config)
    app = config.make_wsgi_app()
    if RLEASE_MODE:
        print('0.0.0.0:80')
        server = make_server('0.0.0.0', 80, app)
    else:
        print('0.0.0.0:8999')
        server = make_server('0.0.0.0', 8999, app)
    server.serve_forever()


if __name__ == '__main__':
    import os
    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
        }
    execute()
