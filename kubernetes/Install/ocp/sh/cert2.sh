source /root/sh/env.sh
cat /root/ocp/pull-secret | jq '.auths += {"host_name": {"auth": "REG_SECRET_INT","email": "beomzh@opennaru.com"}}' | sed "s/REG_SECRET_INT/$REG_SECRET_INT/"|sed "s/host_name/$host_name/" > /root/ocp/pull-secret.json
