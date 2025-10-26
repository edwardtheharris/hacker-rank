# syntax=docker/dockerfile:1
FROM alpine:3.22
LABEL images=name=edwardtheharris/hacker-rank,name=ghcr.io/edwardtheharris/hacker-rank
LABEL source=hacker-rank.edwardtheharris.io.ghcr
RUN apk add --no-cache alpine-sdk bash gcc g++ python3 go shadow
WORKDIR /srv
RUN useradd -s /bin/bash -g users -m -d /home/hacker-rank hacker-rank
USER hacker-rank
CMD [/bin/bash]
