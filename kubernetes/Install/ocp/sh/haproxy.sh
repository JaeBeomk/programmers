source /root/sh/env.sh
cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg_bak

cat << eof > /etc/haproxy/haproxy.cfg
#---------------------------------------------------------------------
# Example configuration for a possible web application.  See the
# full configuration options online.
#
#   https://www.haproxy.org/download/1.8/doc/configuration.txt
#
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global
    maxconn     20000
    log         /dev/log local0 info
    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
    mode                    http
    log                     global
    option                  httplog
    option                  dontlognull
    option http-server-close
    option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          300s
    timeout server          300s
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 20000

frontend openshift-api-server
    bind *:6443
    default_backend openshift-api-server
    mode tcp
    option tcplog

backend openshift-api-server
    balance source
    mode tcp
    server bootstrap ${bootstap}:6443 check fall 3 rise 2
    server master-1 ${master1}:6443 check fall 3 rise 2
    server master-2 ${master2}:6443 check fall 3 rise 2
    server master-3 ${master3}:6443 check fall 3 rise 2


frontend machine-config-server
    bind *:22623
    default_backend machine-config-server
    mode tcp
    option tcplog

backend machine-config-server
    balance source
    mode tcp
    server bootstrap ${bootstap}:22623 check fall 3 rise 2
    server master-1 ${master1}:22623 check fall 3 rise 2
    server master-2 ${master2}:22623 check fall 3 rise 2
    server master-3 ${master3}:22623 check fall 3 rise 2

frontend ingress-http
    bind *:80
    default_backend ingress-http
    mode tcp
    option tcplog

backend ingress-http
    balance source
    mode tcp
    server worker-1 ${worker1}:80 check fall 3 rise 2
    server worker-2 ${worker2}:80 check fall 3 rise 2
    server infra-1 ${infra1}:80 check fall 3 rise 2


frontend ingress-https
    bind *:443
    default_backend ingress-https
    mode tcp
    option tcplog

backend ingress-https
    balance source
    mode tcp
    server worker-1 ${worker1}:443 check fall 3 rise 2
    server worker-2 ${worker2}:443 check fall 3 rise 2
    server infra-1 ${infra1}:443 check fall 3 rise 2
eof
sudo systemctl enable --now haproxy
