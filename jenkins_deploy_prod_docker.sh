#!/bin/sh

#ssh -T ip172-18-0-80-cma6gi5np9tg00enrr8g@direct.labs.play-with-docker.com <<EOF
ssh -T root@buildkitsandbox <<EOF
  git pull
  cd docker1/
  docker compose up -d
  exit
EOF