# node-port -> TCP 트래픽 혀용
# 방화벽 규칙 생성
gcloud compute firewall-rules create test-node-port  --allow tcp:NODE_PORT

# 방화벽 규칙 삭제
gcloud compute firewall-rules delete test-node-port


ex) deploy -> svc -> port open
k create deployment jenkins --image=jenkins/jenkins:lts-jdk17 --port=8080
k expose deployment jenkins --type=NodePort --port=80 --target-port=8080
gcloud compute firewall-rules create test-node-port  --allow tcp:31518

