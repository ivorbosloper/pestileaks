#!/bin/bash

if [ $# -lt 2 ]; then
  echo "$0 <name> <prefixpath>"
  exit 1
fi

NAME=$1                                           # Name of the application
DJANGODIR="$2/pestileaks"                         # Django project directory
SOCKFILE="$2/run/gunicorn.sock"                   # we will communicte using this unix socket
NUM_WORKERS=5                                     # how many worker processes should Gunicorn spawn = 2*numcpu + 1
DJANGO_SETTINGS_MODULE=pestileaks.settings        # which settings file should Django use
DJANGO_WSGI_MODULE=pestileaks.wsgi                # WSGI module name
 
echo "Starting $NAME"
 
# Activate the virtual environment
cd $DJANGODIR
source ../env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=pestileaks --group=pestileaks \
  --log-level=debug \
  --bind=unix:$SOCKFILE
