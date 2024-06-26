# node-port -> TCP 트래픽 혀용
# 방화벽 규칙 생성
gcloud compute firewall-rules create $NAME  --allow tcp:$NODE_PORT

# 방화벽 규칙 삭제
gcloud compute firewall-rules delete $NAME


ex) deploy -> svc -> port open
k create deployment jenkins --image=jenkins/jenkins:lts-jdk17 --port=8080
k expose deployment jenkins --type=NodePort --port=80 --target-port=8080
gcloud compute firewall-rules create tc-lb-port  --allow tcp:31634

