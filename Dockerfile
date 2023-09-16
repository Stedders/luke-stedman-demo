FROM ubuntu:latest
LABEL authors="stedders"

ENTRYPOINT ["top", "-b"]