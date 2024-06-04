# 네트워크 파일시스템
# 서버 설치
apt-get update
apt-get install nfs-common nfs-kernel-server portmap


# 공유 dir 생성
mkdir /home/nfs
chmod 777 /home/nfs

# /etc/exports 파일에 내용추가 
# 해당 IP는 node IP
echo "
/home/nfs 10.128.0.11(rw,sync,no_subtree_check) 10.128.0.12(rw,sync,no_subtree_check) 10.128.0.10(rw,sync,no_subtree_check)
" >> /etc/exports 


service nfs-server restart
showmount -e 127.0.0.1

# nfs 클라이언트에서 mount 명령어로 마운트 후 사용
mount -t nfs 10.0.2.5:/home/nfs/mnt
