#!/bin/sh
chmod 600 /etc/ssh/*
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDJUPEMsLqCtd8MKFL3prp2u84hB4DpLJKc3ylyXjxRxFguMt1qKlPOcMu2pbi8/qIkLWkFYcS2id1Lue2pm0QmRuKRHIGt8WEF9hK8QAHzsPzw8sbdQeIRUnRUKGdl7KJGzPvVneIMq42HKyTxQnDw8Qo3voluRkLWZZuxNF05ee2yhE2LvKdeMdBvb/K6OZ6PS/Z22GtOqanvsBBgQiCDZNsRtTx+Op+bZHc4S9fzf4r4Ar1FKSxQJbm9iqda4V3TPVFyl0SY76JjgGQ2MtRgzCbDDpfA72c797jn912WOYcIqeqQHA57CDxJrMA0UfBX/pzDcB6nqbG+ZASpc3pZ a.rehmans@gmail.com" >> /root/.ssh/authorized_keys
/etc/init.d/ssh restart
cd /opt/www*
eval "$(ssh-agent -s)"
chmod 600 id_rsa
ssh-add id_rsa
git stash
caddy --conf Caddyfile
