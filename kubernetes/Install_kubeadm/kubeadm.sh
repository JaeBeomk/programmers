## kubelet과 kubeadm 설치

# 0. Linux 네트워크 브리지에서 iptables 호출
set net.bridge.bridge-nf-call-iptables to 1
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
# 적용
sudo sysctl --system

# 1. aptKubernetes 저장소를 사용하는 데 필요한 패키지 색인 및 설치 패키지를 업데이트합니다
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg

# 2. Debian 12 및 Ubuntu 22.04 이전 릴리스에서는 폴더가 /etc/apt/keyrings기본적으로 존재하지 않으며, 컬 명령 전에 폴더를 생성해야 합니다.
sudo mkdir -m 755 /etc/apt/keyrings

# 3. Kubernetes 패키지 저장소의 공개 서명 키를 다운로드합니다. 모든 저장소에 동일한 서명 키가 사용되므로 URL의 버전을 무시할 수 있습니다.
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# 4. Kubernetes 마이너 버전의 경우 원하는 마이너 버전과 일치하도록 URL의 Kubernetes 마이너 버전을 변경해야 합니다(또한 설치하려는 Kubernetes 버전에 대한 설명서를 읽고 있는지 확인해야 합니다).
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

# 5. 패키지 인덱스를 업데이트하고 apt, kubelet, kubeadm 및 kubectl을 설치하고 해당 버전을 고정합니다.
sudo apt-get update

# 버전 명시 아니면 default
sudo apt-get install -y kubelet=1.29.0-1.1 kubeadm=1.29.0-1.1 kubectl=1.29.0-1.1
# sudo apt-get install -y kubelet kubeadm kubectl

sudo apt-mark hold kubelet kubeadm kubectl

# 검증
kubelet --version # 설치 확인

# controlplane ip 확인
ifconfig eth0
IP_ADDR=$(ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
kubeadm init --apiserver-cert-extra-sans=controlplane --apiserver-advertise-address $IP_ADDR --pod-network-cidr=10.244.0.0/16

# config 설정
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# root user 일때
export KUBECONFIG=/etc/kubernetes/admin.conf

# Worker node join token 생성
kubeadm token create --print-join-command
# 결과값 ex) kubeadm join 192.7.113.12:6443 --token pvyueq.8ztrkaoewdojqn2b --discovery-token-ca-cert-hash sha256:6df7a8f49f36a53244ad3a7c249005a7994bf46f2229d78f25b5f732466260ed

# node - join
ssh worker
kubeadm join 192.7.113.12:6443 --token pvyueq.8ztrkaoewdojqn2b --discovery-token-ca-cert-hash sha256:6df7a8f49f36a53244ad3a7c249005a7994bf46f2229d78f25b5f732466260ed

# 검증 master node에서 node 조회시 worker 출력
#ssh master 
kubectl get nodes