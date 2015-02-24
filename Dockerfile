FROM resin/rpi-raspbian:latest
RUN apt-get update
RUN apt-get install -y python python-pip python-dev python-dbus
RUN apt-get install -y dropbear
COPY . /app
CMD ["bash", "/app/start.sh"]
