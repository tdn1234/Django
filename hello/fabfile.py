import os

from fabric.api import cd, env, run, task
from fabric.contrib.project import rsync_project

env.host_string = '192.168.73.131'
env.user = 'django'
env.password = '111111'
env.site_path = '/home/django/Downloads/Django/hello'


@task
def deploy():
    deploy_dist()


@task
def hello():
    with cd('/home/django/Downloads'):
        run('rm -rf Django')
        run('git clone git@github.com:tdn1234/Django.git')

    with cd('/home/django/Downloads/Django/'):
        run('rm -rf django')
        run('mkdir django')
        run('cd django')
        run('virtualenv django')
        run('source django/bin/activate')

    with cd('/home/django/Downloads/Django/hello'):
        run('make test')
        run('make install')


@task
def deploy_dist():
    rsync_project(
        local_dir='ukcpa/static',
        remote_dir=os.path.join(env.site_path, 'ukcpa'),
        extra_opts='--checksum',
        delete=True,
    )
