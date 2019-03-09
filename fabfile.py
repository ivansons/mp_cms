from __future__ import unicode_literals

from datetime import datetime
import json
import os
from StringIO import StringIO
from textwrap import dedent
from time import time, sleep
import uuid

from fabric.api import env, local, run, cd, get, put, sudo
from fabric.context_managers import settings, hide
from fabric.decorators import runs_once, task
from fabric.utils import abort, puts

env.roledefs = {
    'prodBETA': ['prodBETA-www-0.matterport.com',
                 'prodBETA-www-1.matterport.com',
                 'prodBETA-www-2.matterport.com',
                 'prodBETA-www-3.matterport.com'],
    'qa1': ['qa1-www-0.matterport.com', 'qa1-www-1.matterport.com'],
    'qa2': ['qa2-www-0.matterport.com'],
    'dev-www-1': ['dev-www-1.matterport.com'],
    'dev-www-2': ['dev-www-2.matterport.com'],
    'dev-www-3': ['dev-www-3.matterport.com'],
    'dev-www-4': ['dev-www-4.matterport.com'],
}

role_config = {
    'vagrant': {
        'work_dir': '/mp_cms',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.dev" '
               'PGUSER="mp_cms" '
               'PGPASSWORD="matterport"',
        'python': '/home/vagrant/venv/bin/python',
    },
    'qa1': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    },
    'qa2': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    },
    'dev-www-1': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    },
    'dev-www-2': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    },
    'dev-www-3': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    },
    'dev-www-4': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    },
    'prodBETA': {
        'work_dir': '/srv/mp_apps/mp_cms/code',
        'env': 'DJANGO_SETTINGS_MODULE="project.settings.server"',
        'python': '/srv/mp_apps/mp_cms/virtualenv/bin/python',
    }
}


def get_current_role():
    for role in env.roledefs.keys():
        if env.host_string in env.roledefs[role]:
            return role


def get_current_role_config():
    if env.get('is_vagrant'):
        return role_config['vagrant']
    role = get_current_role()
    if not role or role not in role_config.keys():
        return abort('Unknown role')
    return role_config[role]


def check_host(allow_prod=False):
    if not env.host_string:
        return abort('Define a host to deploy to,'
                     'e.g. fab deploy -H dev-www-1')
    if not any(host in env.host_string
               for host in ('dev', 'qa', '127.0.0.1')) and not allow_prod:
        return abort('fab deploy should only be used on dev/qa instances')
    if not any(sub_str in env.host_string for sub_str in ('.', 'localhost')):
        env.host_string = '{}.matterport.com'.format(env.host_string)


def run_django_command(command):
    config = get_current_role_config()
    with cd(config['work_dir']):
        run('{} {} manage.py {}'.format(config['env'], config['pm'], command))


def run_django_code(command, verbose=False, use_sudo=False):
    config = get_current_role_config()
    fn = os.path.join('~', '.fab_django_command_{}.py'.format(time()))
    code = dedent("""
        import sys
        import django
        sys.path.append('{}')
        django.setup()
        """.format(config['work_dir'])) + dedent(command)
    hide_args = ('running',) if not verbose else ()
    with hide(*hide_args):
        put(local_path=StringIO(code), remote_path=fn)
        with settings(warn_only=True):
            try:
                func = sudo if use_sudo else run
                return func('{} {} {}'.format(config['env'],
                                              config['python'],
                                              fn),
                            pty=False,
                            combine_stderr=False)
            finally:
                run('rm {}'.format(fn))


@task
@runs_once
def dump_database():
    check_host(allow_prod=True)

    filename = '{}.{}.sql.bz2'.format(env.host_string,
                                      datetime.now().strftime('%Y-%m-%d'))
    remote_path = os.path.join('~', filename)
    local_path = os.path.join('db', filename)

    database_settings = json.loads(run_django_code("""
        from django.conf import settings
        import json
        print json.dumps(settings.DATABASES['default'])
    """, verbose=False, use_sudo=True))

    put(local_path=os.path.join('bin', 'sanitize_sql.py'),
        remote_path=os.path.join('~', 'sanitize_sql.py'))

    database_host = ' -h {HOST}'.format(
            **database_settings) if database_settings.get('HOST') else ''
    database_port = ' -p {PORT}'.format(
            **database_settings) if database_settings.get('PORT') else ''
    database_connection = '{}{}'.format(database_host, database_port)
    dump_cmd = 'PGPASSWORD="{PASSWORD}" ' \
               'pg_dump -U {USER}{database_connection} {NAME} ' \
               '| python sanitize_sql.py | bzip2 > {remote_path}'

    puts('Running pg_dump...')
    with hide('running'):
        run(dump_cmd.format(database_connection=database_connection,
                            remote_path=remote_path,
                            **database_settings))
    run('rm sanitize_sql.py')

    get(remote_path=remote_path, local_path=local_path)
    run('rm {}'.format(remote_path))


@task
@runs_once
def upload_database(db_file):
    config = get_current_role_config()
    check_host()
    puts('Uploading database file...')
    db_command = '{} manage.py dbshell'.format(config['python'])
    remote_tmp_dir = os.path.join('/', 'tmp', 'mp_cms-dump', uuid.uuid4().hex)
    remote_db = os.path.join(remote_tmp_dir, 'upload.db')
    remote_db_bz2 = '{}.bz2'.format(remote_db)
    run('mkdir -p {}'.format(remote_tmp_dir))
    put(local_path=db_file, remote_path=remote_db_bz2)
    with settings(warn_only=True):
        with cd(config['work_dir']):
            run('bzip2 -d {}'.format(remote_db_bz2))
            sudo('cat {} | {} {}'.format(remote_db,
                                         config['env'],
                                         db_command))
    run('rm -r {}'.format(remote_tmp_dir))


@task
def vagrant():
    config = dict(line.split() for line in local('vagrant ssh-config',
                                                 capture=True).splitlines())
    env.user = config['User']
    env.hosts = ['{}:{}'.format(config['HostName'], config['Port'])]
    env.key_filename = config['IdentityFile'].strip('"')
    env.is_vagrant = True


@task
def deploy(enable_node=True):
    """
    Deploy the current version of mp_cms to the specified environment
    or host.

    Don't mark this as parallel unless you know what you're doing!

    Example Usage:
      fab deploy -R qa1
      fab deploy -H dev-www-1
    """
    check_host(allow_prod=True)
    print('Deploying to {}'.format(env.host_string))
    sudo('salt-call saltutil.sync_all')
    print('Removing {} from loadbalancer.'.format(env.host_string))
    sudo('salt-call state.sls mp_apps.mp_cms.health_check_off')
    # Sleep 60 seconds to be sure we are out of rotation.
    sleep(60)
    # Bug: CMS-852
    sudo('salt-call state.sls mp_apps.mp_cms')
    # Kinda odd, but all nodes run pre-deploy.
    sudo('salt-call state.sls mp_apps.mp_cms.pre_deploy')
    if enable_node is True:
        print('Putting {} back into loadbalancer.'.format(env.host_string))
        sudo('salt-call state.sls mp_apps.mp_cms.health_check_on')
