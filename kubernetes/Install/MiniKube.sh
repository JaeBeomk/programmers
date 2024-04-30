# VM 환경에 minikube 구성

# 1. docker 설치
sudo apt install docker.io -y
# 권한 변경
sudo usermod -aG docker $USER && newgrp docker

# 조회 테스트
docker ps -a

# 2. minikube설치
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb

# 실행 테스트
minikube start --driver=docker

# minikub에 클라이언트로 접속하기 위한 kubectl snap 설치
sudo snap install kubectl

# 조회 테스트
kubectl get nodes

# 3. minikube SSH
minikube ssh

