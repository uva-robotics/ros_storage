FROM uva/ros_core

RUN apt-get update && \
    apt-get install -y \
    python-mysqldb

COPY src/main.py /root
