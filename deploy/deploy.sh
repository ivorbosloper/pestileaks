cd /home/pestileaks/pestileaks
git pull origin master
. ../env/bin/activate 
pip install -r doc/requirements.txt
./manage.py collectstatic --noinput
