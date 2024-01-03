#!/bin/sh

git pull
cd docker1/
docker compose up -d

#ssh -T root@buildkitsandbox <<EOF
#ssh -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com <<EOF
#  git pull
#  cd docker1/
#  docker compose up -d
#  exit
#EOF
