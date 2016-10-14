# Create Django secret key and pass it as an env variable.
# The env variable is read in local_settings.py.
export DJANGO_SECRET_KEY=`python -c "import random,string;print ''.join([random.SystemRandom().choice('{}{}{}'.format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)])"`

docker run -itd --name pestileaks \
 --hostname pestileaks \
 -v /opt/pestileaks/run:/home/pestileaks/run \
 -e DJANGO_SECRET_KEY \
 crop-r/pestileaks
