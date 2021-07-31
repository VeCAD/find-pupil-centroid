FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    autoconf \
    automake \
    libtool \
    build-essential \
    git\
    unzip \
    pkg-config \
    python-setuptools \
    python-dev \
    libomp-dev \
    python3-opencv \
    python3-numpy \
    nano \
    python3-pip \
    libopencv-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libgtk2.0-dev \
    qt5-default \
    libcanberra-gtk-module \
    libcanberra-gtk3-module

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /pupil_detect

ENTRYPOINT ["python3", "pupil_detect.py"]
