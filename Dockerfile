FROM ubuntu:trusty

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir -p /usr/app
WORKDIR /usr/app

COPY requirements.txt /usr/app/requirements.txt
RUN pip3 install -r requirements.txt

ENV BEEDRIVER_BROWSER=remote

CMD python3 -m behave
