#!/bin/sh
cd /opt/www*
eval "$(ssh-agent -s)"
chmod 600 /opt/keys/id_rsa
ssh-add /opt/keys/id_rsaid_rsa
caddy --conf Caddyfile
