# coding: utf-8

"""Imaging-viewer system setup & deploy.

This script supply blow functions for ubuntu.
    - provisioning
    - deployment

* You need to prepare server passing TCP/22 ubuntu server.

***COMMAND(Deploy)***
ubuntu$ fab -H xx.xx.xx.xx [-i ~/.ssh/hogehoge.pem] deploy

***COMMAND(Provision)***
ubuntu$ fab -H xx.xx.xx.xx [-i ~/.ssh/hogehoge.pem] provision

"""

from os import path
from fabric.api import run
from fabric.api import cd
from fabric.api import env
from fabric.api import sudo
from fabric.api import local
from fabric.api import lcd
from fabric.contrib import files
from fabric.colors import yellow


# ---- ENVIRONMENT ----
env.user = 'ubuntu'
env.password = 'ubuntu'
env.warn_only = True

# ---- MODULE VARIABLES ----
REPOGITORY = 'image-viewer'
REPOGITORY_OWNER = 'pyohei'


def deploy():
    """Script deploy."""
    print yellow('--- START DEPLOY ---')
    if not files.exists(REPOGITORY):
        url = 'https://github.com/{owner}/{repo}.git'.format(
            owner=REPOGITORY_OWNER,
            repo=REPOGITORY)
        __clone(url, submodule=True)
    else:
        with cd(REPOGITORY):
            run('git pull')
    with cd(REPOGITORY):
        sudo('rsync --delete -a -v -r ./ /var/www/piyokkuma/')
    print yellow('--- FINISH DEPLOY ---')


def provision():
    """Provision the environment.

    Execute ansible command.
    """
    basepath = path.dirname(path.abspath(__file__))
    with lcd(basepath):
        __provision()
    deploy()


def __provision():
    local('ansible-playbook -i hosts playbook.yml -k ')


def __clone(path, submodule=False):
    command = 'git clone '
    if submodule:
        command += '--recursive '
    command += path
    run(command)
