FROM ubuntu:trusty

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir -p /usr/app
WORKDIR /usr/app

COPY requirements.txt /usr/app/requirements.txt
RUN pip3 install -r requirements.txt

CMD sleep inf
#CMD BEEDRIVER_CONFIG=custom_config BEEDRIVER_BROWSER=remote python3 -m behave features/livechat_feature_switch.feature
