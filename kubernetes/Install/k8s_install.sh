# 저장소 설정
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 도커 공식 GPG key추가
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Stable repository 설정
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 도커엔진 / containerd 설치
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# docker version 확인
sudo docker version

# docker 서비스 등록 및 실행
sudo systemctl enable docker
sudo systemctl start docker

# k8s 설치
# 1) 메모리 스왑
sudo swapoff -a && sudo sed -i '/swap/s/^/#/' /etc/fstab

# 2) 노드간 통신을 위한 iptables에 브릿지 관련 설정 추가
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF
 
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system

# 3) 방화벽 비활성
sudo ufw disable

# kubeadm/kubelet/kubectl 설치 아래 링크 참고
# https://kubernetes.io/ko/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

# 구글 퍼블릭키 다운
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

# 쿠버네티스 gpg 및 소스 리스트 내용 추가 및 apt 업데이트
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl


# systemd 와 cgroup 설정 맞추기
sudo mkdir /etc/docker
cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF

# k8s 서비스 등록 및 재시작
sudo systemctl daemon-reload
sudo systemctl restart kubelet