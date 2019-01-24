FROM ubuntu:latest
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

RUN adduser -D myuser
USER myuser

	
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
