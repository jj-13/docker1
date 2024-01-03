#!/bin/sh

eval $(ssh-agent -s)
ssh-add /etc/ssh/ssh_host_ed25519_key

#ssh -T root@buildkitsandbox <<EOF
ssh -o StrictHostKeyChecking=no -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com <<EOF
  git pull
  cd docker1/
  docker compose up -d
  exit
EOF
