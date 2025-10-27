# syntax=docker/dockerfile:1
FROM alpine:3.22
LABEL images=name=edwardtheharris/hacker-rank,name=ghcr.io/edwardtheharris/hacker-rank
LABEL source=hacker-rank.edwardtheharris.io.ghcr
# RUN apk add --no-cache alpine-sdk=1.1-r0 bash-completion=2.16.0-r0 bash==5.2.37 gcc=14.2.0 g++=14.2.0 python3=3.12.12 go=1.29.9 shadow=4.17.3-r0
RUN apk add --no-cache \
  alpine-sdk \
  bash \
  bash-completion \
  g++ \
  gcc \
  go \
  python3 \
  shadow
WORKDIR /srv
RUN useradd -s /bin/bash -g users -m -d /home/hacker-rank hacker-rank
USER hacker-rank
CMD ["/bin/bash"]
