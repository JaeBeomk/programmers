# 모든 node
sudo swapoff -a # 현재 시스템에 적용(리부팅하면 재설정 필요)
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab # 리부팅 필수

sudo reboot
