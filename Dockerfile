FROM python:3.6-alpine3.7
LABEL maintainer="hwvwvi@gmail.com"

# APK repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# Copy pip requirements.txt
COPY ./requirements.txt /requirements.txt

# Install Chromium && selenium
RUN apk update && \
    apk add chromium chromium-chromedriver && \
    pip install -r /requirements.txt
