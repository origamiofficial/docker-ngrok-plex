FROM python:slim-buster

# environment settings
WORKDIR /root
ENV PLEX_BaseURL 'http://172.17.0.1:32400'
ENV PLEX_Token 'XXXXXXXXXX'
ENV NGROK_Token 'XXXXXXXXXX'

# update & install ngrok
RUN pip install --upgrade pip
RUN pip install PlexAPI
RUN apt update
RUN apt install curl cron -y
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
    && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list \
    && apt update \
    && apt install ngrok -y

# copy script files
COPY ["docker-entrypoint.sh", "ngrok-plex.py", "./"]
RUN chmod +x docker-entrypoint.sh

# target run
ENTRYPOINT ["./docker-entrypoint.sh"]
