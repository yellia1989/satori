FROM ubuntu:18.04
MAINTAINER feisuzhu@163.com
ARG USE_MIRROR

ENV TERM xterm
RUN echo "199.232.28.133 raw.githubusercontent.com" >> /etc/hosts
RUN echo "104.18.121.25 production.cloudflare.docker.com" >> /etc/hosts
ADD sources.list /etc/apt/sources.list
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN adduser ubuntu
RUN [ -z "$USE_MIRROR" ] || (sed -E -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list; touch /etc/use-mirror)
RUN apt-get update --fix-missing && apt-get install -y tzdata curl fcgiwrap supervisor git python3 python3-pip python3-venv redis-server openjdk-11-jre-headless locales
RUN locale-gen zh_CN.UTF-8
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN:en
ENV LC_ALL zh_CN.UTF-8

