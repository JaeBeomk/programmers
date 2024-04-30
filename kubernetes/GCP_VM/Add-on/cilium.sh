# master-node 실행
# cilium 다운로드
# add-on를 기동해줘야 container가 기동될수있다.
curl -LO https://github.com/cilium/cilium-cli/releases/latest/download/cilium-linux-amd64.tar.gz
sudo tar xzvfC cilium-linux-amd64.tar.gz /usr/local/bin
rm cilium-linux-amd64.tar.gz
cilium install

# 상태 체크
# cilium status
