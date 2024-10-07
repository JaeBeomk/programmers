sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf
mkdir -pv /var/www/html/ocp
chmod -R 755 /var/www/html/ocp/
systemctl enable --now httpd
