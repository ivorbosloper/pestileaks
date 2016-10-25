cd /home/pestileaks/pestileaks
git pull origin live_2013
git checkout live_2013
# This branch's doc/requirements.txt is missing some dependencies. Use requirements.txt from the master branch.
git fetch
git checkout origin/master -- doc/requirements.txt
. ../env/bin/activate 
pip install -r doc/requirements.txt
./manage.py collectstatic --noinput
