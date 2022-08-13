# ngrok-plex ![Docker Pulls](https://img.shields.io/docker/pulls/rlabinc/ngrok-plex.svg?style=flat&label=pulls&logo=docker) ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/rlabinc/ngrok-plex/latest.svg?style=flat&label=image&logo=docker) ![GitHub Repo stars](https://img.shields.io/github/stars/origamiofficial/ngrok-plex?style=social)

[ngrok-plex](https://gist.github.com/nagleaidan/dcc132c16d15565d88bf2d9200351c6e) is a command line utility to run Plex through ngrok to bypass CGNAT or Double-NAT scenario.

## Supported Architectures

We utilise the docker buildx for multi-platform awareness. More information is available from docker [here](https://docs.docker.com/buildx/working-with-buildx/).

Simply pulling `rlabinc/ngrok-plex:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64-\<version tag\> |
| armhf| ✅ | arm32v7-\<version tag\> |

## Usage
You will have to extract the Plex token sets for you and provide it to the CLI. But don't worry, I'll guide you through the entire process.
## Extracting the Plex token
- Go to any media in your Plex library.
- Go to the Kebab Menu (⋮)
- Click on `Get Info`
- Click on `View XML` — a new tab should open up.
- Go to the very end of the URL. You should see a 20 character string after `X-Plex-Token=`. Copy this string.

Here are the commands you'll need:

```bash
docker run -d \
  --name=ngrok-plex \
  -e TZ=Europe/London `#optional` \
  -e PLEX_BaseURL='http://127.0.0.1:32400' `#better to use single quotes` \
  -e PLEX_Token='XXXXXXXXXX' `#better to use single quotes` \
  -e NGROK_Token='XXXXXXXXXX' `#better to use single quotes` \
  rlabinc/ngrok-plex:latest
```

A cronjob will update new ngrok URL every 6 hours.

## Parameters

Container images are configured using parameters passed at runtime (such as those above).

| Parameter | Function |
| :----: | --- |
| `-e TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `-e PLEX_BaseURL='http://127.0.0.1:32400'` | Specify Plex URL to use. |
| `-e PLEX_Token='XXXXXXXXXX'` | Specify Plex token to use. |
| `-e NGROK_Token='XXXXXXXXXX'` | Specify ngrok token to use. |

## Github Repository
https://github.com/origamiofficial/ngrok-plex

## Docker Hub
https://hub.docker.com/r/rlabinc/ngrok-plex

## Acknowledgements
All credit goes to [@nagleaidan](https://github.com/nagleaidan). Special thanks to [@Rihcus](https://github.com/Rihcus) for fixing many issues.

## Warning
Use of this software may constitute a breach in the [ngrok Terms of Service](https://ngrok.com/tos). Use at your own risk.
