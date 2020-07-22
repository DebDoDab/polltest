FROM python:3.8.3
MAINTAINER debbius3@gmail.com

WORKDIR /usr/shr/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./app ./app

WORKDIR ./app
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8002", "polltest.wsgi:application"]