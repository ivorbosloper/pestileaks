FROM ubuntu:16.04

RUN useradd -m pestileaks && echo "pestileaks:pestileaks" | chpasswd && adduser pestileaks sudo

RUN echo "Europe/Amsterdam" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y unzip nano redis-server

# TODO nog nodig? locales voor postgres fixen
RUN apt-get install -y language-pack-en locales && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# RUN apt-get best practices: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#/apt-get
RUN apt-get update && apt-get install -y \
    binutils \
    python-psycopg2 python-setuptools gettext python-dev python-geoip \
    python-virtualenv \
    libffi-dev python-dev \
    libtiff-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk \
    libssl-dev libcurl4-openssl-dev \
    libxml2-dev libxslt1-dev python-dev libpcre3-dev \
    git \
    supervisor \
    postgresql-9.5 postgresql-contrib-9.5 postgresql-client-9.5 postgresql-9.5-postgis-2.2 postgresql-server-dev-9.5 \
&& rm -rf /var/lib/apt/lists/*

ENV DATABASE_NAME pestileaks
ENV DATABASE_USER pestileaks
USER postgres
# RUN cp ${DATADIR}scan_project/config/postgresql/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf
RUN echo 'local     all    pestileaks   trust' >> /etc/postgresql/9.5/main/pg_hba.conf
RUN /etc/init.d/postgresql start &&\
    createuser -sl ${DATABASE_USER} &&\
    psql --command "update pg_database set datistemplate=false where datname='template1';" &&\
    dropdb template1 &&\
    createdb template1 --owner=postgres --encoding='UTF-8' --lc-collate='en_US.UTF-8' --lc-ctype='en_US.UTF-8' --template=template0 &&\
    psql --command "update pg_database set datistemplate=true where datname='template1';" &&\
    createdb --encoding='UTF-8' --locale='en_US.UTF-8' ${DATABASE_NAME} 

# TODO config logrotate
# RUN cp ${DATADIR}project/config/logrotate/* /etc/logrotate.d/

# install pestileaks
USER pestileaks
WORKDIR /home/pestileaks
RUN git clone https://github.com/ivorbosloper/pestileaks.git
RUN virtualenv --no-site-packages env
COPY local_settings_container.py /home/pestileaks/pestileaks/pestileaks/local_settings.py
COPY deploy.sh /home/pestileaks/pestileaks
RUN mkdir /home/pestileaks/run
RUN . /home/pestileaks/pestileaks/deploy.sh

# Config supervisor to run pestileaks
USER root
COPY supervisor/pestileaks.conf /etc/supervisor/conf.d/

VOLUME /home/pestileaks/run

COPY entrypoint.sh /opt/docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "/opt/docker-entrypoint.sh"]

