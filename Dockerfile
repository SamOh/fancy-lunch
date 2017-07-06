FROM python:3.6

RUN apt-get update -y \
 && apt-get upgrade -y \
 && apt-get autoremove -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY src/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY src /usr/src/app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "3", "-k", "gevent", "wsgi"]