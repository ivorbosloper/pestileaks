docker run -itd --name pestileaks \
 --hostname pestileaks \
 -v /home/cropr/components/pestileaks/docker-run:/home/pestileaks/run \
 -p 127.0.0.1:8002:80 \
 crop-r/pestileaks
