# 임시 pod 생성 후 명령 예시
kubectl run -it test-pod --image=busybox --rm --restart=Never --command -- curl 127.0.0.1
