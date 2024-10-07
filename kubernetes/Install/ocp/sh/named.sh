source /root/sh/env.sh
sed -i 's/listen-on port 53 { 127.0.0.1; };/listen-on port 53 { any; };/g' /etc/named.conf
sed -i 's/allow-query     { localhost; };/allow-query     { any; };/g' /etc/named.conf
cat <<EOF >> /etc/named.rfc1912.zones
zone "${sub_domain}.${domain}.${TLD}" IN {
    type master;
    file "${sub_domain}.${domain}.${TLD}.zone";
    allow-update { none; };
};

zone "200.168.192.in-addr.arpa" IN {
    type master;
    file "${sub_domain}.${domain}.${TLD}.rev";
    allow-update { none; };
};
EOF
cat <<EOF > /var/named/${sub_domain}.${domain}.${TLD}.zone
\$TTL 1D
@       IN SOA  @ ${host_name}. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum

; name servers - NS records
        NS     ${host_name}.

; OpenShift Container Platform Cluster - A records
master-1        IN      A       ${master1}
master-2        IN      A       ${master2}
master-3        IN      A       ${master3}
worker-1        IN      A       ${worker1}
worker-2        IN      A       ${worker2}
infra-1         IN      A       ${infra1}
bootstrap       IN      A       ${bootstap}
bastion         IN      A       ${bastion}

; OpenShift internal cluster IPs - A records
api             IN      A    ${bastion}
api-int         IN      A    ${bastion}
*.apps          IN      A    ${bastion}
EOF

cat <<EOF > /var/named/${sub_domain}.${domain}.${TLD}.rev
\$TTL 1D
@       IN SOA  @ ${host_name}. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
; name servers - NS records
        NS     ${host_name}.

; OpenShift Container Platform Cluster - PTR records
${lbr}     IN      PTR   bootstrap.${sub_domain}.${domain}.${TLD}.
${lm1}     IN      PTR   master-1.${sub_domain}.${domain}.${TLD}.
${lm2}     IN      PTR   master-2.${sub_domain}.${domain}.${TLD}.
${lm3}     IN      PTR   master-3.${sub_domain}.${domain}.${TLD}.
${lw1}     IN      PTR   worker-1.${sub_domain}.${domain}.${TLD}.
${lw2}     IN      PTR   worker-2.${sub_domain}.${domain}.${TLD}.
${li1}     IN      PTR   infra-1.${sub_domain}.${domain}.${TLD}.
${lbt}      IN      PTR  api.${sub_domain}.${domain}.${TLD}.
${lbt}      IN      PTR  api-int.${sub_domain}.${domain}.${TLD}.
EOF
