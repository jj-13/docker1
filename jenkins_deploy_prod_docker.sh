#!/bin/sh

eval $(ssh-agent -s) && ssh-add jenkins_agent

#ssh -T root@buildkitsandbox <<EOF
ssh -o StrictHostKeyChecking=no -T ip172-18-0-49-cmarr0dnp9tg009crrr0@direct.labs.play-with-docker.com <<EOF
  git pull
  cd docker1/
  docker compose up -d
  exit
EOF
