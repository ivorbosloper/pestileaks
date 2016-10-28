#!/bin/bash

HOSTNAME=`cat /etc/hostname`

# hack to make sure this directory is writable by user pestileaks
chown pestileaks:pestileaks /home/pestileaks/run

# make sure the logs directory exists
mkdir /home/pestileaks/run/logs
chown pestileaks:pestileaks /home/pestileaks/run/logs

#cron -f &
service postgresql start
#service memcached start
/etc/init.d/supervisor start
service nginx start
#/etc/init.d/redis-server start
#/etc/init.d/geoserver start
bash
