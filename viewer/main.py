"""Simple imager server"""

import csv
import os
from pyramid.renderers import render_to_response

PORT = 8999
USER = 'user'
PASSWD = 'password'

PUBLIC_DIR = None

def _disp_login(request, error='', del_cookies=[]):
    """Display login interface."""
    params = {}
    params['error'] = error
    response = render_to_response(
        'login.mak',
        params,
        request=request)
    if del_cookies:
        for c in del_cookies:
            response.delete_cookie(c)
    return response


def _disp_images(request):
    """Display images."""
    params = request.POST
    is_login = False
    if 'username' in params and 'userpass' in params:
        username = params['username']
        userpass = params['userpass']
        is_login = _can_login(username, userpass)
    if 'sid' in request.cookies:
        sid = request.cookies['sid']
        is_login = _has_valid_cookie(sid)
    if not is_login:
        return _disp_login(request, u'Failur in login!!!')
    image_paths = []
    for r, d, fs in os.walk(PUBLIC_DIR):
        for f in fs:
            _p = os.path.join(r, f)
            _f = _p.replace(PUBLIC_DIR, '').lstrip('/')
            image_paths.append(os.path.join('images', _f))
    params = {}
    params['images'] = image_paths
    response = render_to_response(
        'images.mak',
        params,
        request=request)
    response.set_cookie('sid', 'iv')
    return response


def _logout(request):
    """Delete cookie for logout."""
    return _disp_login(request, del_cookies=['sid'])


def _can_login(username, userpass):
    """Check user name and password."""
    return username == USER and userpass == PASSWD


def _has_valid_cookie(cookie):
    """Check cookie value."""
    return cookie == 'iv'


def _add_routes(config):
    """Add Root information."""
    config.add_route('login', '/login')
    config.add_view(_disp_login, route_name='login')
    config.add_route('images', '/images')
    config.add_view(_disp_images, route_name='images')
    config.add_route('logout', '/logout')
    config.add_view(_logout, route_name='logout')
    config.add_static_view('static', 'static')
    config.add_static_view('images', PUBLIC_DIR)


def execute():
    """Execute this application."""
    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    config = Configurator()
    config.include('pyramid_mako')
    _add_routes(config)
    app = config.make_wsgi_app()
    print('Access to http://localhost:{}/login'.format(PORT))
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description='Simple image viewer.')
    p_h = 'Public image directory. If you want to see sample, input `images/sample`'
    p.add_argument('public_dir', help=p_h)
    args = p.parse_args()
    PUBLIC_DIR = os.path.abspath(args.public_dir)
    if not os.path.isdir(PUBLIC_DIR):
        print('public_dir doesn\'t exist!')
        quit()

    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
        }
    execute()
