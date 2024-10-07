source /root/sh/env.sh
chmod 644 /var/named/${sub_domain}.${domain}.${TLD}.*

named-checkconf /etc/named.conf
named-checkconf /etc/named.rfc1912.zones
named-checkzone ${sub_domain}.${domain}.${TLD} /var/named/${sub_domain}.${domain}.${TLD}.zone
systemctl enable --now named

echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
echo "bastion서버 dns 추가해주세요!!!"
