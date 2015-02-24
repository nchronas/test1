FROM resin/rpi-raspbian:wheezy
RUN apt-get update
RUN apt-get install -y python python-pip python-dbus
ADD server_example.py /app/
RUN echo 'python /app/server_example.py' > /start
RUN chmod +x /start
