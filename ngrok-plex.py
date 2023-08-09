#!/usr/bin/python3

from plexapi.server import PlexServer
import os
import sys
import json
import requests
import time
import socket

# Script version
SCRIPT_VERSION = "1.1"

###This script hashes out the duckdns portion. 

# please make sure to install PlexAPI via pip, "pip install PlexAPI"
# makesure to update the duckdns url with token and domainname
# don't forget to add your plex token
# follow https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
# need time for ngrok to start up before requesting data
print("Waiting 5 seconds for ngrok to start up")
time.sleep(5)

def get_ngrok_port():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    for i in res_json["tunnels"]:
        if i['proto'] == 'tcp':
            return i['public_url'].split(':')[-1]

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    for i in res_json["tunnels"]:
        if i['proto'] == 'tcp':
            return i['public_url'].split(':')[-2]

# get and clean up ngrok tcp url for later (this code is messy) :(
ngrokurl=get_ngrok_url()
ngrokurlclean= ngrokurl.split('//')[-1]
print("ngrok base url = " + ngrokurlclean)

# get ngrok url ip
ngrokip = socket.gethostbyname(ngrokurlclean)
print("ngrok url and ip no port = " + ngrokip)

#update duckdns with ngrok ip make sure to change [] or copy url from duckdns install guide
### duckdnsupdateurl="https://www.duckdns.org/update?domains=[yourname]&token=[yourapitoken]&ip=" + ngrokip
### res = requests.get(duckdnsupdateurl)
### print(res.status_code)

def build_url_list():
    NGROK_PORT = get_ngrok_port()
### NGROK_BASES = ["https://[yourname].duckdns.org:"]
    NGROK_BASES = ["http://" + ngrokip + ":"] # Comment this line out if you are using a domain with duckdns line 54
    NGROK_URLS = [base + NGROK_PORT for base in NGROK_BASES]
    CUSTOM_URL = ""
    for url in NGROK_URLS:
        CUSTOM_URL += url + ", "
    CUSTOM_URL = CUSTOM_URL[:-2]
    return CUSTOM_URL

# Load user defined config"
PLEX_BaseURL = os.environ['PLEX_BaseURL']
PLEX_Token = os.environ['PLEX_Token']

# stores plex user login info into a variable
plex = PlexServer(PLEX_BaseURL, PLEX_Token)

# displays current plex custom url settings. Not needed but nice to see
print("Old settings: " + plex.settings.customConnections)

# sets plex's "Custom server access URLs" with one from Ngrok
customUrl = plex.settings.get('customConnections')
customUrl.set(build_url_list())
plex.settings.save()

# displays new custom plex url from Ngrok. Not needed but nice to see
plex = PlexServer(PLEX_BaseURL, PLEX_Token)
print("New settings: " + plex.settings.customConnections)