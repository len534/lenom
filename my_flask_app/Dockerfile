FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
RUN useradd -m myuser
USER myuser
CMD ["app.py","gunicorn --bind 0.0.0.0:$PORT wsgi"]
