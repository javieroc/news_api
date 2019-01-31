FROM python:3.7-slim

ADD . /srv/app
WORKDIR /srv/app

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install python3-dev \
    && apt-get -y install iputils-ping \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt --src /usr/local/src

RUN chmod +x ./start.sh
CMD ["./start.sh"]