# PROJECT_ID == gcloud config get-value project 명령어로 확인
# image는 방금 생성한 Artififact Registry에 저장

# image 생성
gcloud builds submit \
  --tag us-central1-docker.pkg.dev/[PROJECT_ID]/hello-repo/helloworld-gke .

# image 삭제
gcloud artifacts docker images delete \
    us-central1-docker.pkg.dev/PROJECT_ID/hello-repo/helloworld-gke