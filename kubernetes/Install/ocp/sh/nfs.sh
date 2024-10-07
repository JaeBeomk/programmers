source /root/sh/env.sh
systemctl enable --now nfs-server
mkdir -pv /var/nfsshare
chown -R nobody:nobody /var/nfsshare/  #RHEL7 경우 nfsnobody:nfsnobody
echo '/var/nfsshare ${bastion}/24(rw,sync,root_squash)' >> /etc/exports
exportfs -r
systemctl restart nfs-server
