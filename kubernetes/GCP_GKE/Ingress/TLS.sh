# TLS 인증서 생성
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -out ingress-tls.crt \
    -keyout ingress-tls.key \
    -subj "/CN=ingress-tls"

# tls인증서 사용하는 secret 생성
kubectl create secret tls ingress-tls \
    --namespace default \
    --key ingress-tls.key \
    --cert ingress-tls.crt