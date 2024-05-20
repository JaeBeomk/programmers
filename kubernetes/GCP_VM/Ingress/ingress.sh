# 인그레스는 하나의 IP이나 도메인으로 다수의 서비스 제공
# 인그레스의 필요성
# 프라이빗 환경에서 인그레스를 사용할 수 있는 ingress-nginx를 설치
# 쿠버네티스에 파드 형태로 띄워서 설정하는 방법 확인
# nginx-ingress를 파드로 떠있으면서 다시 서비스로 연결할 수 있는 역할을 수행

git clone https://github.com/kubernetes/ingress-nginx/
kubectl apply -k `pwd`/ingress-nginx/deploy/static/provider/baremetal/
# 마지막 명령은 webhook 구성을 삭제함, 이 기능으로 ingress가 정상적으로 구동되지 않는 현상이있음
kubectl delete validatingwebhookconfigurations.admissionregistration.k8s.io ingress-nginx-admission
