FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-dev python3-pip build-essential
COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]
CMD gunicorn -b :$PORT main:app

