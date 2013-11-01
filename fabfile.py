from __future__ import with_statement
from fabric.api import local, abort, run, cd, env
from fabric.context_managers import prefix

env.directory = '/home/pestileaks/pestileaks'
env.activate = 'source /home/pestileaks/env/bin/activate'
env.user = 'pestileaks'
env.hosts = ['pestileaks.nl']
env.restart = 'killall -HUP gunicorn'
    
#Show current status versus current github master state
def status():
    with cd(env.directory):
        run('git status')

def deploy():
    with cd(env.directory):
        run("git pull")
        #run("rm -rf /home/pestileaks/run/static")
        run("mkdir -p /home/pestileaks/run/static")

        with prefix(env.activate):
            run("if [ doc/requirements.txt -nt doc/requirements.pyc ]; then pip install -r doc/requirements.txt; touch doc/requirements.pyc; fi")
            run('./manage.py syncdb')
            run('./manage.py migrate --noinput')
            run('./manage.py collectstatic --noinput')

    run(env.restart)
