#!/usr/bin/python3
""" Fabric script (file 1-pack_web_static.py) -> distributes archive """

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['100.25.220.124', '54.160.81.217']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """ Do -> Deploy """
    try:
        if not (path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}\
                        /web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'.format(timestamp))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except Exception as e:
        return False

    return True
