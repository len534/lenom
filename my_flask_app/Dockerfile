FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

RUN adduser -D myuser
USER myuser

	
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
