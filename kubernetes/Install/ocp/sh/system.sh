systemctl  disable --now firewalld
systemctl enable --now chronyd
timedatectl set-timezone Asia/Seoul
