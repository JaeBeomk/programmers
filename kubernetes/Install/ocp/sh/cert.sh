source /root/sh/env.sh
mkdir -pv /opt/registry/{auth,certs,data}
cd /opt/registry/certs
openssl req -addext "subjectAltName=DNS:${host_name}" -subj "/C=KO/ST=Seoul/L=Seoul/O=Opennaru/OU=support/CN=${host_name}/emailAddress=beomzh@opennaru.com" -newkey rsa:4096 -nodes -sha256 -keyout domain.key -x509 -days 365 -out domain.crt 
cp domain.crt /etc/pki/ca-trust/source/anchors/.

sleep 5; echo "update-ca-trust start"
update-ca-trust

mkdir /root/ocp
