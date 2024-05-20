# bash-completion은 /etc/bash_completion.d 에 있는 모든 자동 완성 스크립트를 소싱한다.

# k8s tab키 사용시 자동완성(현재 사용자만)
source <(kubectl completion bash)
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
echo "source <(kubectl completion bash)" >> ~/.bashrc

# 시스템 전체에 적용
kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
source ~/.bashrc

