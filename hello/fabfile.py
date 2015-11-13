import os

from fabric.api import env, run, task
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
    run('cd /home/django/Downloads/')
    # run('git clone git@github.com:tdn1234/Django.git')
    run('cd Django/')
    run('mkdir django')
    run('cd django')
    run('virtualenv django')
    run('source django/bin/activate')
    run("cd %s" % env.site_path)
    run('make install')

@task
def deploy_dist():
    rsync_project(
        local_dir='ukcpa/static',
        remote_dir=os.path.join(env.site_path, 'ukcpa'),
        extra_opts='--checksum',
        delete=True,
    )
