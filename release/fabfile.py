# coding: utf-8

"""Imaging-viewer system setup & deploy.

This script supply blow functions for ubuntu.
    - provisioning
    - deployment

* You need to prepare server passing TCP/22 ubuntu server.

***COMMAND(Deploy)***
ubuntu$ fab -H xx.xx.xx.xx [-i ~/.ssh/hogehoge.pem] deploy_[bat|sync|www]

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
REPOGITORY_bat = 'rirakkuma-crawller'
REPOGITORY_sync = 'encryptfile'
REPOGITORY_www = 'image-viewer'
REPOGITORY_OWNER = 'pyohei'


def deploy_bat():
    """Script deploy.(bat)"""
    print yellow('--- START DEPLOY ({0}) ---'.format(REPOGITORY_bat))
    if not files.exists(REPOGITORY_bat):
        url = 'https://github.com/{owner}/{repo}.git'.format(
            owner=REPOGITORY_OWNER,
            repo=REPOGITORY_bat)
        __clone(url, submodule=True)
    else:
        with cd(REPOGITORY_bat):
            run('git pull')
    print yellow('--- FINISH DEPLOY ---')


def deploy_sync():
    """Script deploy.(sync)"""
    print yellow('--- START DEPLOY ({0}) ---'.format(REPOGITORY_sync))
    if not files.exists(REPOGITORY_sync):
        url = 'https://github.com/{owner}/{repo}.git'.format(
            owner=REPOGITORY_OWNER,
            repo=REPOGITORY_sync)
        __clone(url, submodule=True)
    else:
        with cd(REPOGITORY_sync):
            run('git pull')
    print yellow('--- FINISH DEPLOY ---')


def deploy_www():
    """Script deploy.(www)"""
    print yellow('--- START DEPLOY ({0}) ---'.format(REPOGITORY_www))
    if not files.exists(REPOGITORY_www):
        url = 'https://github.com/{owner}/{repo}.git'.format(
            owner=REPOGITORY_OWNER,
            repo=REPOGITORY_www)
        __clone(url, submodule=True)
    else:
        with cd(REPOGITORY_www):
            run('git pull')
    with cd(REPOGITORY_www):
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
