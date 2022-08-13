#!/bin/bash

# setting up ngrok
ngrok config add-authtoken $NGROK_Token

# cron settings to update ngrok url
echo -e "0 */6 * * *    root    /bin/python3 /root/ngrok-plex.py" >> /etc/crontab
cron

# target run
ngrok tcp 32400 & python3 ./ngrok-plex.py

# keep the container running
sleep infinity
